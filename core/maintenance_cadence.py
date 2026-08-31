#!/usr/bin/env python3
"""Deterministic local maintenance-cadence scanner for epistemic-pipeline.

The scanner reports maintenance evidence only. It does not mutate inspected
source/configuration/history files, call GitHub, dereference remote sources,
run tests, validate scientific truth, or convert heuristic scores into
probability. When ``--output`` is supplied, it writes only the caller-requested
report file and records that write request in the report boundaries.

``maintenance/cadence.yaml`` is JSON-compatible YAML and is parsed with the
Python standard library.
"""

from __future__ import annotations

import argparse
import calendar
import hashlib
import json
import re
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable, Optional

PROFILE = "epistemic-pipeline/maintenance-report"
DEFAULT_CONFIG = Path("maintenance/cadence.yaml")
TEXT_SUFFIXES = {".md", ".py", ".yaml", ".yml", ".json", ".toml"}


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def _load_config(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("maintenance cadence configuration must be an object")
    return data


def _repo_relative(root: Path, path: Path) -> Optional[str]:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return None


def _configuration_reference(root: Path, config_path: Path) -> tuple[str, str]:
    relative = _repo_relative(root, config_path)
    if relative is not None:
        return relative, "repo-local"
    return f"external:{config_path.name}", "external"


def _resolve_repo_entry(root: Path, value: Any) -> tuple[str, Path]:
    text = str(value).strip()
    if not text:
        raise ValueError("path entry must be non-empty")
    raw = Path(text)
    if raw.is_absolute() or ".." in raw.parts:
        raise ValueError("path entry must be repository-relative and must not contain '..'")
    resolved = (root / raw).resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError as exc:
        raise ValueError("path entry resolves outside repository root") from exc
    return raw.as_posix(), resolved


def _validated_entries(
    root: Path,
    values: Iterable[Any],
    *,
    field: str,
    findings: list[dict[str, Any]],
) -> list[tuple[str, Path]]:
    result: list[tuple[str, Path]] = []
    seen: set[Path] = set()
    for value in values:
        try:
            display, resolved = _resolve_repo_entry(root, value)
        except ValueError as exc:
            findings.append(
                {
                    "severity": "error",
                    "kind": "maintenance-config-path-outside-repository",
                    "field": field,
                    "value": str(value),
                    "detail": str(exc),
                }
            )
            continue
        if resolved in seen:
            findings.append(
                {
                    "severity": "warning",
                    "kind": "duplicate-maintenance-config-path",
                    "field": field,
                    "path": display,
                }
            )
            continue
        seen.add(resolved)
        result.append((display, resolved))
    return result


def _validated_patterns(
    values: Iterable[Any],
    *,
    findings: list[dict[str, Any]],
) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        text = str(value).strip()
        raw = Path(text)
        if not text or raw.is_absolute() or ".." in raw.parts:
            findings.append(
                {
                    "severity": "error",
                    "kind": "maintenance-history-pattern-outside-repository",
                    "value": text,
                }
            )
            continue
        normalized = raw.as_posix()
        if normalized in seen:
            continue
        seen.add(normalized)
        result.append(normalized)
    return result


def _iter_text_files(entries: Iterable[tuple[str, Path]]) -> Iterable[tuple[str, Path]]:
    seen: set[Path] = set()
    for display, candidate in entries:
        if candidate.is_file() and candidate.suffix.lower() in TEXT_SUFFIXES:
            resolved = candidate.resolve()
            if resolved not in seen:
                seen.add(resolved)
                yield display, candidate
        elif candidate.is_dir():
            for path in sorted(candidate.rglob("*")):
                if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
                    resolved = path.resolve()
                    if resolved not in seen:
                        seen.add(resolved)
                        child_display = (Path(display) / path.relative_to(candidate)).as_posix()
                        yield child_display, path


def _manifest_calibrated(root: Path) -> Optional[str]:
    path = root / "MANIFEST.yaml"
    if not path.is_file():
        return None
    match = re.search(
        r"(?m)^calibrated:\s*[\"']?(\d{4}-\d{2}-\d{2})",
        path.read_text(encoding="utf-8"),
    )
    return match.group(1) if match else None


def _age_days(value: Optional[str], as_of: date) -> Optional[int]:
    if not value:
        return None
    try:
        parsed = datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        return None
    return (as_of - parsed).days


def _parse_date(value: Any) -> Optional[date]:
    if not value:
        return None
    try:
        return datetime.strptime(str(value), "%Y-%m-%d").date()
    except ValueError:
        return None


def _calendar_month_status(as_of: date) -> str:
    last_day = calendar.monthrange(as_of.year, as_of.month)[1]
    return "calendar-month-close" if as_of.day == last_day else "month-to-date"


def _stage_status(config: dict, as_of: date) -> dict:
    stage = dict(config.get("stage") or {})
    start = _parse_date(stage.get("window_start"))
    close = _parse_date(stage.get("close_date"))
    if start and as_of < start:
        status = "not-started"
    elif close and as_of >= close:
        status = "closed"
    else:
        status = "active"
    return {
        "id": stage.get("id"),
        "window_start": start.isoformat() if start else None,
        "close_date": close.isoformat() if close else None,
        "status": status,
        "close_semantics": stage.get("close_semantics"),
    }


def _history_inventory(
    root: Path,
    patterns: Iterable[str],
    findings: list[dict[str, Any]],
) -> list[str]:
    found: set[str] = set()
    for pattern in patterns:
        for path in root.glob(pattern):
            if not path.is_file():
                continue
            relative = _repo_relative(root, path)
            if relative is None:
                findings.append(
                    {
                        "severity": "error",
                        "kind": "maintenance-history-match-outside-repository",
                        "pattern": pattern,
                        "path": path.as_posix(),
                    }
                )
                continue
            found.add(path.relative_to(root).as_posix())
    return sorted(found)


def build_report(
    *,
    root: Path,
    config_path: Path,
    cadence: str,
    as_of: date,
    report_output_path: Optional[Path] = None,
) -> dict:
    root = root.resolve()
    config_path = config_path.resolve()
    config = _load_config(config_path)
    cadences = config.get("cadences") or {}
    if cadence not in cadences:
        raise ValueError(f"unsupported cadence {cadence!r}; choose from {sorted(cadences)}")
    cadence_config = dict(cadences[cadence])

    findings: list[dict[str, Any]] = []
    canonical_entries = _validated_entries(
        root,
        config.get("canonical_paths") or [],
        field="canonical_paths",
        findings=findings,
    )
    scan_entries = _validated_entries(
        root,
        config.get("scan_paths") or [],
        field="scan_paths",
        findings=findings,
    )
    governance_entries = _validated_entries(
        root,
        config.get("forbidden_governance_paths") or [],
        field="forbidden_governance_paths",
        findings=findings,
    )
    history_patterns = _validated_patterns(
        config.get("history_patterns") or [],
        findings=findings,
    )

    canonical_paths = [display for display, _ in canonical_entries]
    missing = [display for display, path in canonical_entries if not path.exists()]
    for path in missing:
        findings.append({"severity": "error", "kind": "missing-canonical-path", "path": path})

    governance_present = [display for display, path in governance_entries if path.exists()]
    for path in governance_present:
        findings.append({
            "severity": "error",
            "kind": "forbidden-governance-path-present",
            "path": path,
            "semantics": "GitHub-native merge-gate automation is outside the research architecture",
        })

    prefix = str(config.get("project_profile_prefix") or "")
    pattern = re.compile(
        re.escape(prefix) + r"[A-Za-z0-9._/-]+(?:@\d+|/v\d+)\b"
    ) if prefix else None
    pseudo_versions: list[dict[str, Any]] = []
    if pattern:
        for display, path in _iter_text_files(scan_entries):
            text = path.read_text(encoding="utf-8", errors="replace")
            matches = sorted(set(pattern.findall(text)))
            if matches:
                record = {"path": display, "matches": matches}
                pseudo_versions.append(record)
                findings.append({"severity": "error", "kind": "decorative-project-version", **record})

    calibrated = _manifest_calibrated(root)
    calibration_age = _age_days(calibrated, as_of)
    max_age = int(cadence_config.get("calibration_max_age_days", 0) or 0)
    if calibration_age is None:
        findings.append({"severity": "warning", "kind": "manifest-calibration-date-unavailable"})
    elif calibration_age < 0:
        findings.append({"severity": "warning", "kind": "manifest-calibration-date-in-future", "calibrated": calibrated})
    elif max_age and calibration_age > max_age:
        findings.append({
            "severity": "warning",
            "kind": "frontier-calibration-stale-for-cadence",
            "calibrated": calibrated,
            "age_days": calibration_age,
            "maximum_age_days": max_age,
        })

    baseline_hashes: dict[str, str] = {}
    if cadence_config.get("baseline_hashes"):
        for display, path in canonical_entries:
            if path.is_file():
                baseline_hashes[display] = _sha256(path)

    history_snapshots = (
        _history_inventory(root, history_patterns, findings)
        if cadence_config.get("history_inventory")
        else []
    )

    severity_counts = {"error": 0, "warning": 0, "info": 0}
    for finding in findings:
        severity = str(finding.get("severity") or "info")
        severity_counts[severity] = severity_counts.get(severity, 0) + 1

    config_ref, config_scope = _configuration_reference(root, config_path)
    output_requested = report_output_path is not None
    output_inside_repo: Optional[bool] = None
    if report_output_path is not None:
        output_inside_repo = _repo_relative(root, report_output_path.resolve()) is not None

    return {
        "profile": PROFILE,
        "cadence": cadence,
        "as_of": as_of.isoformat(),
        "purpose": cadence_config.get("purpose"),
        "configuration": config_ref,
        "configuration_scope": config_scope,
        "configuration_file_sha256": _sha256(config_path),
        "period_status": {
            "calendar_month": _calendar_month_status(as_of),
            "stage": _stage_status(config, as_of),
        },
        "checks": {
            "canonical_path_count": len(canonical_paths),
            "missing_canonical_paths": missing,
            "forbidden_governance_paths_present": governance_present,
            "decorative_project_versions": pseudo_versions,
            "manifest_calibrated": calibrated,
            "manifest_calibration_age_days": calibration_age,
            "repository_scope_enforced": True,
        },
        "findings": findings,
        "finding_counts": severity_counts,
        "baseline_sha256": baseline_hashes,
        "history_snapshots": history_snapshots,
        "maintenance_boundaries": {
            "inspected_files_mutated": False,
            "report_output_write_requested": output_requested,
            "report_output_inside_repository": output_inside_repo,
            "history_rewrite_performed": False,
            "automatic_deletion_performed": False,
            "remote_dereference_performed": False,
            "tests_run_by_scanner": False,
            "github_actions_used": False,
            "scan_scope_outside_repository_permitted": False,
            "absolute_repository_root_embedded": False,
            "aggregate_score": None,
            "scientific_validity_claim": False,
            "provenance_soundness_claim": False,
            "probability_claim": False,
        },
        "semantics": (
            "local deterministic maintenance evidence only; repository-local paths are emitted relative to the "
            "repository root and configuration identity is hashed. Calendar/stage close status is temporal "
            "metadata, and clean maintenance structure does not establish claim truth, evidence sufficiency, "
            "provenance soundness, calibrated probability, peer review, or reproduction"
        ),
    }


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Run local daily/weekly/monthly evidence-pipeline maintenance checks")
    parser.add_argument("cadence", choices=["daily", "weekly", "monthly"])
    parser.add_argument("--root", default=".")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--as-of", help="YYYY-MM-DD, defaults to local current date")
    parser.add_argument("--output", help="optional JSON report path")
    args = parser.parse_args(argv)

    as_of = datetime.strptime(args.as_of, "%Y-%m-%d").date() if args.as_of else date.today()
    root = Path(args.root).resolve()
    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = root / config_path
    output_path = Path(args.output).resolve() if args.output else None

    report = build_report(
        root=root,
        config_path=config_path,
        cadence=args.cadence,
        as_of=as_of,
        report_output_path=output_path,
    )
    payload = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 1 if report["finding_counts"].get("error", 0) else 0


if __name__ == "__main__":
    raise SystemExit(main())
