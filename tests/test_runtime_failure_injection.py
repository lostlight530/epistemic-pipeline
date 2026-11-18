"""Deterministic failure injection for caller timeout, retry and checkpoint boundaries.

These checks observe local mechanism behavior; they do not imply durable,
external-effect-safe execution, forced thread cancellation, or scientific validity.
"""
import json
import tempfile
import threading
import unittest
from pathlib import Path

from core.engine import StateMachineEngine
from core.resilience import (
    NodeTimeoutError, RetryPolicy, run_with_retry, run_with_timeout,
)


ROOT = Path(__file__).resolve().parents[1]


class RuntimeFailureInjection(unittest.TestCase):
    def test_timeout_bounds_wait_but_does_not_kill_worker_thread(self):
        started = threading.Event()
        release = threading.Event()
        finished = threading.Event()

        def slow_work():
            started.set()
            release.wait(timeout=2)
            finished.set()
            return "late-success"

        try:
            with self.assertRaises(NodeTimeoutError):
                run_with_timeout(slow_work, 0.05)
            self.assertTrue(started.wait(timeout=1))
            self.assertFalse(finished.is_set())
        finally:
            release.set()
        self.assertTrue(finished.wait(timeout=1))

    def test_retry_only_explicit_transient_failures(self):
        attempts = []

        def unstable():
            attempts.append("called")
            if len(attempts) < 3:
                raise ConnectionError("temporary fixture")
            return {"ok": True}

        result = run_with_retry(
            unstable,
            RetryPolicy(max_attempts=3, base_delay=0, max_delay=0),
        )
        self.assertEqual(result, {"ok": True})
        self.assertEqual(len(attempts), 3)

    def test_unknown_failure_is_not_replayed(self):
        attempts = []

        def permanent():
            attempts.append("called")
            raise RuntimeError("unknown effect state")

        with self.assertRaises(RuntimeError):
            run_with_retry(
                permanent, RetryPolicy(max_attempts=4, base_delay=0, max_delay=0),
            )
        self.assertEqual(len(attempts), 1)

    def test_checkpoint_resume_binds_graph_digest_and_run_path(self):
        with tempfile.TemporaryDirectory() as td:
            engine = StateMachineEngine(
                str(ROOT / "graphs" / "linear.yaml"),
                mock_llm=True, checkpoint_dir=td, trace_dir=None,
            )
            fixture = {"discover": {"status": "success", "outputs": {"source": "fixture"}}}
            engine._write_checkpoint("safe-run", fixture)
            self.assertEqual(engine._load_checkpoint("safe-run"), fixture)
            with self.assertRaises(ValueError):
                engine._checkpoint_path("../escape")

            checkpoint = engine._checkpoint_path("safe-run")
            recorded = json.loads(checkpoint.read_text(encoding="utf-8"))
            recorded["graph_sha256"] = "sha256:wrong-graph"
            checkpoint.write_text(json.dumps(recorded), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "graph digest mismatch"):
                engine._load_checkpoint("safe-run")

    def test_checkpoint_rejects_legacy_missing_digest(self):
        with tempfile.TemporaryDirectory() as td:
            engine = StateMachineEngine(
                str(ROOT / "graphs" / "linear.yaml"),
                mock_llm=True, checkpoint_dir=td, trace_dir=None,
            )
            path = engine._checkpoint_path("legacy")
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                json.dumps({
                    "run_id": "legacy", "graph_id": engine.graph_data.get("id"),
                    "results": {"discover": {"status": "success"}},
                }), encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "lacks graph_sha256"):
                engine._load_checkpoint("legacy")



    def test_checkpoint_writer_preserves_legacy_staging_symlink_target(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            protected = root / "protected.txt"
            protected.write_text("PRESERVE", encoding="utf-8")
            engine = StateMachineEngine(
                str(ROOT / "graphs" / "linear.yaml"),
                mock_llm=True, checkpoint_dir=str(root / "checkpoints"),
                trace_dir=None,
            )
            checkpoint = engine._checkpoint_path("safe-run")
            checkpoint.parent.mkdir(parents=True, exist_ok=True)
            old_stage = checkpoint.with_suffix(".json.tmp")
            try:
                old_stage.symlink_to(protected)
            except (OSError, NotImplementedError) as exc:
                self.skipTest(f"symbolic links unavailable: {exc}")

            engine._write_checkpoint(
                "safe-run", {"discover": {"status": "success", "outputs": {}}}
            )
            self.assertEqual(protected.read_text(encoding="utf-8"), "PRESERVE")
            self.assertTrue(old_stage.is_symlink())
            self.assertEqual(
                json.loads(checkpoint.read_text(encoding="utf-8"))["run_id"],
                "safe-run",
            )


if __name__ == "__main__":
    unittest.main()
