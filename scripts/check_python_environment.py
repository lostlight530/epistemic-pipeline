#!/usr/bin/env python3
"""Validate the version-pinned Python 3.13 verification environment, offline.

This checks installed distributions, not wheel hashes, artifact identity,
cross-platform portability, scientific validity, or independent reproduction.
"""
from __future__ import annotations

import argparse
import importlib.metadata
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def inspect(path: Path) -> dict:
    expected = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("==")
        if len(parts) != 2 or not all(parts):
            raise ValueError(f"not an exact name==version pin: {line!r}")
        package, version = parts
        expected[package] = version
    actual = {}
    failures = []
    for package, version in sorted(expected.items()):
        try:
            installed = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            installed = None
        actual[package] = installed
        if installed != version:
            failures.append({"package": package, "expected": version, "installed": installed})
    py_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    python_match = py_version == "3.13"
    return {
        "python": py_version,
        "python_match": python_match,
        "pin_file": path.name,
        "checked_distributions": len(expected),
        "mismatches": failures,
        "match": python_match and not failures,
        "limitations": "version set only; wheel hashes, OS and external runtimes are not verified",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--requirements", type=Path,
        default=ROOT / "requirements-python313.txt",
    )
    args = parser.parse_args()
    result = inspect(args.requirements)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0 if result["match"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
