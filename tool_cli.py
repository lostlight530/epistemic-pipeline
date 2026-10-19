#!/usr/bin/env python3
"""Unified local tool console: machine JSON, terminal report, offline HTML.

This CLI is a thin presentation/transport wrapper around agent_tools.py. It
does not start a network server, install an external agent, or execute code
specified by user-provided names.
"""
from __future__ import annotations

import argparse
import html
import json
import os
from pathlib import Path
import sys
import tempfile
from typing import Any

from agent_tools import PROFILE, TOOL_SPECS, execute_tool_call, tool_definitions


def _domain_failed(payload: dict) -> bool:
    if payload.get("status") != "ok":
        return True
    result = payload.get("result")
    return isinstance(result, dict) and (
        result.get("diagnostic_exit_code", 0) != 0
        or result.get("valid") is False
        or result.get("check_status") == "failed"
    )


def _human(payload: dict, color: bool) -> str:
    fail = _domain_failed(payload)
    label = "CHECK FAILED" if fail else "EXECUTED"
    def tint(value: str, code: str) -> str:
        return "\x1b[" + code + "m" + value + "\x1b[0m" if color else value
    lines = [
        tint("╭─ RESEARCH TOOLS  /  LOCAL CONSOLE ──────────────────╮", "1;36"),
        "│  " + tint(label, "1;31" if fail else "1;32"),
        "│  PROFILE  " + str(payload.get("profile", "")),
        "│  TOOL     " + str(payload.get("tool", "-")),
        tint("╰───────────────────────────────────────────────────╯", "1;36"),
        json.dumps(payload.get("result") if not fail or payload.get("result") is not None
                   else payload.get("error"), ensure_ascii=False, indent=2, sort_keys=True),
    ]
    return "\n".join(lines) + "\n"


def _html_report(payload: dict) -> str:
    fail = _domain_failed(payload)
    title = html.escape(str(payload.get("tool") or "Tool catalog"))
    profile = html.escape(str(payload.get("profile", "")))
    status = "CHECK FAILED" if fail else "EXECUTED"
    pretty = html.escape(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    # No scripts, remote fonts, trackers or unescaped caller content.
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · Research Tools</title>
<style>
:root {{color-scheme:light dark;--bg:#f5f8fc;--panel:#fff;--fg:#14243a;--muted:#526579;--edge:#dbe5f0;--accent:#0876b9;--code:#edf5fc;--bad:#b7313a;--good:#117d55}}
@media(prefers-color-scheme:dark){{:root{{--bg:#101827;--panel:#172437;--fg:#edf3fa;--muted:#b1c2d4;--edge:#2b4058;--accent:#7cccf9;--code:#101d2c;--bad:#ff818a;--good:#5ee0a6}}}}
*{{box-sizing:border-box}}body{{margin:0;font:15px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif;background:var(--bg);color:var(--fg)}}
main{{max-width:980px;margin:auto;padding:clamp(20px,5vw,60px)}}header{{display:flex;align-items:center;gap:13px;color:var(--accent);font-size:12px;font-weight:800;letter-spacing:.12em;text-transform:uppercase}}
header i{{display:block;width:13px;height:13px;border:3px solid currentColor;border-radius:4px;transform:rotate(45deg)}}
h1{{font-size:clamp(25px,4vw,38px);line-height:1.18;margin:25px 0 12px;overflow-wrap:anywhere}}.sub{{color:var(--muted);margin:0 0 25px;overflow-wrap:anywhere}}
article{{background:var(--panel);border:1px solid var(--edge);border-radius:16px;overflow:hidden;box-shadow:0 10px 35px #15283a0a}}
.status{{font-weight:750;padding:15px 24px;border-bottom:1px solid var(--edge);color:var(--good)}}.bad{{color:var(--bad)}}pre{{white-space:pre-wrap;overflow-wrap:anywhere;background:var(--code);font:12.5px/1.65 ui-monospace,SFMono-Regular,Consolas,monospace;margin:20px;padding:22px;border-radius:10px}}
footer{{font-size:12px;color:var(--muted);margin-top:22px}}@media(max-width:520px){{pre{{padding:13px;margin:10px}}}}
</style></head><body><main><header><i aria-hidden="true"></i>RESEARCH TOOLS · LOCAL EVIDENCE</header>
<h1>{title}</h1><p class="sub">{profile} · Explicit tool execution, not independent research verification</p>
<article aria-label="Tool result"><div class="status {'bad' if fail else ''}">{status}</div>
<pre role="region" aria-label="Structured JSON result">{pretty}</pre></article>
<footer>Offline report · no network requests · machine result and domain findings remain distinct</footer>
</main></body></html>
"""


def _write_output(path: str, content: str) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix="." + target.name + ".", dir=str(target.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, target)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def _read_arguments(args: argparse.Namespace) -> dict:
    if args.args_file is not None:
        if args.args_file == "-":
            source = sys.stdin.read(1024 * 1024 + 1)
        else:
            with open(args.args_file, "r", encoding="utf-8") as handle:
                source = handle.read(1024 * 1024 + 1)
    else:
        source = args.args
    if len(source.encode("utf-8")) > 1024 * 1024:
        raise ValueError("tool arguments exceed 1 MiB")
    value = json.loads(source)
    if not isinstance(value, dict):
        raise ValueError("tool arguments must be an object")
    return value


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Research Tools: allowlisted local Agent/CLI console")
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("list", "describe", "invoke"):
        cmd = sub.add_parser(command)
        if command in ("describe", "invoke"):
            cmd.add_argument("tool", help="allowlisted tool name")
        if command == "invoke":
            sources = cmd.add_mutually_exclusive_group()
            sources.add_argument("--args", default="{}", help="JSON object arguments")
            sources.add_argument("--args-file", help="JSON file path or - for stdin")
        cmd.add_argument("--format", choices=["json", "text", "html"], default="json")
        cmd.add_argument("--output", help="write formatted result to a local file")
        cmd.add_argument("--no-color", action="store_true")
    a = parser.parse_args(argv)
    if a.command == "list":
        result = {"profile": PROFILE, "tool": None, "status": "ok",
                  "result": {"tools": tool_definitions()}, "error": None,
                  "scientific_validity_claim": False, "remote_provider_called": False}
    elif a.command == "describe":
        info = TOOL_SPECS.get(a.tool)
        result = {"profile": PROFILE, "tool": a.tool,
                  "status": "ok" if info else "error", "result": info,
                  "error": None if info else {"code": "UNKNOWN_TOOL", "message": "tool is not allowlisted"},
                  "scientific_validity_claim": False, "remote_provider_called": False}
    else:
        try:
            parsed = _read_arguments(a)
            result = execute_tool_call(a.tool, parsed)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            result = {"profile": PROFILE, "tool": a.tool, "status": "error",
                      "result": None, "error": {"code": "INVALID_ARGUMENT", "message": str(exc)},
                      "scientific_validity_claim": False, "remote_provider_called": False}
    if a.format == "json":
        rendered = json.dumps(result, ensure_ascii=False, sort_keys=True) + "\n"
    elif a.format == "text":
        color = (not a.no_color and not os.environ.get("NO_COLOR")
                 and a.output is None and sys.stdout.isatty())
        rendered = _human(result, color)
    else:
        rendered = _html_report(result)
    if a.output:
        try:
            _write_output(a.output, rendered)
        except OSError as exc:
            print(f"OUTPUT_WRITE_FAILED: {exc}", file=sys.stderr)
            return 2
    else:
        sys.stdout.write(rendered)
    return 1 if _domain_failed(result) else 0


if __name__ == "__main__":
    raise SystemExit(main())
