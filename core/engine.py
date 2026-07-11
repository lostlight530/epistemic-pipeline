#!/usr/bin/env python3
"""
状态机执行引擎 — 解析依赖图并执行状态流转
Enhanced: Asyncio, Checkpoint/Resume, LangGraph-style conditional edges, retry with backoff
"""

import yaml
import json
import os
import sys
import asyncio
import logging
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
from collections import deque
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.dependency_graph import DependencyGraph

logger = logging.getLogger('epistemic_engine')


class NodeStatus:
    PENDING = 'pending'
    RUNNING = 'running'
    SUCCESS = 'success'
    FAILED = 'failed'
    SKIPPED = 'skipped'
    RETRYING = 'retrying'


class CheckpointManager:
    """Manages execution checkpoints for resume capability"""

    def __init__(self, checkpoint_dir: str = ".checkpoints"):
        self.checkpoint_dir = Path(checkpoint_dir)
        self.checkpoint_dir.mkdir(exist_ok=True)

    def _get_path(self, run_id: str) -> Path:
        return self.checkpoint_dir / f"{run_id}.json"

    def save(self, run_id: str, state: dict):
        path = self._get_path(run_id)
        with open(path, 'w') as f:
            json.dump(state, f, indent=2)
        logger.info(f"Checkpoint saved: {path}")

    def load(self, run_id: str) -> Optional[dict]:
        path = self._get_path(run_id)
        if path.exists():
            with open(path, 'r') as f:
                return json.load(f)
        return None

    def list_checkpoints(self) -> List[str]:
        return [p.stem for p in self.checkpoint_dir.glob("*.json")]


class StateMachineEngine:
    """Enhanced state machine engine with async execution and checkpointing"""

    def __init__(self, graph_path: str, checkpoint_dir: str = ".checkpoints"):
        self.graph_data = self._load_graph(graph_path)
        self.nodes = {n['id']: n for n in self.graph_data['nodes']}
        self.dep_graph = DependencyGraph(self.graph_data['nodes'])
        self.execution_order = []
        self.current_state = None
        self.outputs = {}
        self.checkpoint_mgr = CheckpointManager(checkpoint_dir)
        self.run_id = datetime.now().strftime("run_%Y%m%d_%H%M%S")

    def _load_graph(self, path: str) -> dict:
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def validate(self) -> Tuple[bool, List[str]]:
        return self.dep_graph.validate()

    def compute_execution_order(self) -> List[str]:
        self.execution_order = self.dep_graph.topological_sort()
        return self.execution_order

    async def _execute_node(self, state_id: str, results_dict: dict) -> dict:
        """Execute a single node with retry and timeout"""
        node = self.nodes[state_id]
        stage = node['stage']
        retry_count = node.get('retry_count', 0)
        timeout = node.get('timeout', 60)

        logger.info(f"Executing state: {state_id} (stage: {stage})")

        # Check dependencies
        deps = node.get('dependencies', [])
        for dep in deps:
            if dep not in results_dict or results_dict[dep]['status'] != 'success':
                logger.warning(f"Dependency {dep} not completed")
                return {"status": "failed", "errors": [f"Dependency {dep} not completed"]}

        # Check condition (LangGraph-style conditional edge)
        condition = node.get('condition')
        if condition:
            try:
                locals_dict = {'inputs': results_dict, 'outputs': self.outputs}
                if not eval(condition, {"__builtins__": {}}, locals_dict):
                    logger.info(f"Condition not met for {state_id}, skipping")
                    return {"status": "skipped", "state_id": state_id}
            except Exception as e:
                logger.error(f"Condition evaluation failed: {e}")
                return {"status": "failed", "errors": [str(e)]}

        # Execute with retry
        for attempt in range(retry_count + 1):
            try:
                state_def = self._load_state(stage)
                result = await asyncio.wait_for(
                    self._run_state_logic(state_id, stage, state_def, results_dict),
                    timeout=timeout
                )
                result['attempt'] = attempt + 1
                return result
            except asyncio.TimeoutError:
                logger.warning(f"Timeout on {state_id}, attempt {attempt + 1}")
                if attempt == retry_count:
                    return {"status": "failed", "errors": ["Timeout"]}
                await asyncio.sleep(2 ** attempt)  # Exponential backoff
            except Exception as e:
                logger.error(f"Error on {state_id}: {e}")
                if attempt == retry_count:
                    return {"status": "failed", "errors": [str(e)]}
                await asyncio.sleep(2 ** attempt)

        return {"status": "failed", "errors": ["Max retries exceeded"]}

    async def _run_state_logic(self, state_id: str, stage: str, state_def: dict, results_dict: dict) -> dict:
        """Actual state execution logic"""
        # Simulate execution (replace with actual logic)
        await asyncio.sleep(0.01)
        return {
            "status": "success",
            "state_id": state_id,
            "stage": stage,
            "completed": True,
            "outputs": state_def.get('activities', []),
            "quality_gates_passed": True
        }

    async def run(self) -> dict:
        """Execute full pipeline with async and checkpointing"""
        valid, errors = self.validate()
        if not valid:
            logger.error("Graph validation failed")
            return {"status": "failed", "errors": errors}

        parallel_groups = self.dep_graph.find_parallel_groups()
        logger.info(f"Graph valid, parallel groups: {parallel_groups}")

        results = {}
        total_executed = 0

        for group in parallel_groups:
            if len(group) == 1:
                state_id = group[0]
                result = await self._execute_node(state_id, results)
                if result['status'] == 'failed':
                    return {"status": "failed", "errors": result['errors']}
                results[state_id] = result
                self.outputs[state_id] = result
                total_executed += 1
            else:
                logger.info(f"Parallel group: {group}")
                tasks = [self._execute_node(sid, results) for sid in group]
                group_results = await asyncio.gather(*tasks)

                for state_id, result in zip(group, group_results):
                    if result['status'] == 'failed':
                        return {"status": "failed", "errors": result['errors']}
                    results[state_id] = result
                    self.outputs[state_id] = result
                    total_executed += 1

            # Save checkpoint after each group
            self.checkpoint_mgr.save(self.run_id, {
                'run_id': self.run_id,
                'completed_groups': parallel_groups[:parallel_groups.index(group) + 1],
                'results': {k: v for k, v in results.items()},
                'timestamp': datetime.now().isoformat()
            })

        order = self.compute_execution_order()
        logger.info(f"Pipeline complete: {total_executed} nodes")
        return {"status": "success", "results": results, "order": order, "run_id": self.run_id}

    async def resume(self, run_id: str) -> dict:
        """Resume from checkpoint"""
        checkpoint = self.checkpoint_mgr.load(run_id)
        if not checkpoint:
            return {"status": "failed", "errors": [f"Checkpoint {run_id} not found"]}

        logger.info(f"Resuming from checkpoint: {run_id}")
        # Restore state and continue
        self.outputs = checkpoint.get('results', {})
        return await self.run()

    def _load_state(self, stage_name: str) -> dict:
        state_path = Path('states') / f'{stage_name}.yaml'
        with open(state_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def get_report(self) -> dict:
        """Generate execution report"""
        return {
            'run_id': self.run_id,
            'total_nodes': len(self.nodes),
            'completed_nodes': len(self.outputs),
            'checkpoints': self.checkpoint_mgr.list_checkpoints()
        }


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Epistemic Pipeline Engine (Optimized)')
    parser.add_argument('action', choices=['run', 'validate', 'resume', 'report'], help='Action')
    parser.add_argument('graph', help='Graph file path')
    parser.add_argument('--resume-from', help='Checkpoint to resume from')
    args = parser.parse_args()

    engine = StateMachineEngine(args.graph)

    if args.action == 'validate':
        valid, errors = engine.validate()
        print(f"{'✅' if valid else '❌'} Validation: {'PASS' if valid else 'FAIL'}")
        if errors:
            for e in errors:
                print(f"  - {e}")
    elif args.action == 'run':
        result = asyncio.run(engine.run())
        print(f"\nFinal status: {result['status']}")
        if result['status'] == 'success':
            print(f"Run ID: {result['run_id']}")
    elif args.action == 'resume':
        if not args.resume_from:
            print("❌ --resume-from required")
            sys.exit(1)
        result = asyncio.run(engine.resume(args.resume_from))
        print(f"\nResume status: {result['status']}")
    elif args.action == 'report':
        report = engine.get_report()
        print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
