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


    def _enable_weekly_history_inventory(self, config_path: Path) -> None:
        config = json.loads(config_path.read_text(encoding="utf-8"))
        config["history_patterns"] = ["maintenance/*_DAY_CONSOLIDATION.md"]
        config["cadences"]["weekly"] = {
            "calibration_max_age_days": 0,
            "baseline_hashes": False,
            "history_inventory": True,
        }
        config_path.write_text(json.dumps(config), encoding="utf-8")

    def test_external_history_link_finding_is_repository_relative(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            root, config, _ = self._setup(home)
            self._enable_weekly_history_inventory(config)
            outside = home / "outside.md"
            outside.write_text("historical evidence", encoding="utf-8")
            relative = "maintenance/FOUR_DAY_CONSOLIDATION.md"
            self._link(root / relative, outside)

            report = build_report(
                root=root, config_path=config, cadence="weekly", as_of=date(2026, 10, 11)
            )
            matched = [
                f for f in report["findings"]
                if f["kind"] == "maintenance-history-match-outside-repository"
            ]
            self.assertEqual(len(matched), 1)
            self.assertEqual(matched[0]["path"], relative)
            self.assertEqual(report["history_snapshots"], [])
            self.assertNotIn(str(root), json.dumps(report))

    def test_internal_history_file_remains_in_inventory(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            root, config, _ = self._setup(home)
            self._enable_weekly_history_inventory(config)
            relative = "maintenance/FOUR_DAY_CONSOLIDATION.md"
            (root / relative).write_text("historical evidence", encoding="utf-8")

            report = build_report(
                root=root, config_path=config, cadence="weekly", as_of=date(2026, 10, 11)
            )
            self.assertEqual(report["history_snapshots"], [relative])
            self.assertNotIn(
                "maintenance-history-match-outside-repository",
                [f["kind"] for f in report["findings"]],
            )


if __name__ == "__main__":
    unittest.main()
