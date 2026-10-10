#!/usr/bin/env python3
"""Repository-local scan regression: symbolic links must not escape the root."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.maintenance_cadence import PROFILE, build_report


class TestMaintenanceScanScope(unittest.TestCase):
    def _setup(self, home: Path) -> tuple[Path, Path, str]:
        root = home / "repo"
        (root / "maintenance").mkdir(parents=True)
        prefix = PROFILE.split("/", 1)[0] + "/"
        config = {
            "project_profile_prefix": prefix,
            "canonical_paths": [],
            "scan_paths": ["maintenance"],
            "forbidden_governance_paths": [],
            "history_patterns": [],
            "cadences": {"daily": {"calibration_max_age_days": 0}},
        }
        config_path = root / "scan.json"
        config_path.write_text(json.dumps(config), encoding="utf-8")
        return root, config_path, prefix

    def _link(self, path: Path, target: Path) -> None:
        try:
            path.symlink_to(target)
        except (OSError, NotImplementedError) as exc:
            self.skipTest(f"symbolic links unavailable: {exc}")

    def test_external_symlink_is_reported_without_scanning_target(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            root, config, prefix = self._setup(home)
            outside = home / "external.md"
            outside.write_text(prefix + "test-profile@2", encoding="utf-8")
            self._link(root / "maintenance" / "outside-link.md", outside)

            report = build_report(
                root=root, config_path=config, cadence="daily", as_of=date(2026, 10, 10)
            )
            kinds = [item["kind"] for item in report["findings"]]
            self.assertIn("maintenance-scan-file-outside-repository", kinds)
            self.assertNotIn("decorative-project-version", kinds)
            self.assertEqual(report["checks"]["decorative_project_versions"], [])

    def test_internal_symlink_is_still_scanned(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            root, config, prefix = self._setup(home)
            inside = root / "inside.md"
            inside.write_text(prefix + "test-profile@2", encoding="utf-8")
            self._link(root / "maintenance" / "inside-link.md", inside)

            report = build_report(
                root=root, config_path=config, cadence="daily", as_of=date(2026, 10, 10)
            )
            kinds = [item["kind"] for item in report["findings"]]
            self.assertNotIn("maintenance-scan-file-outside-repository", kinds)
            self.assertIn("decorative-project-version", kinds)


if __name__ == "__main__":
    unittest.main()
