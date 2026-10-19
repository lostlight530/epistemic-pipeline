.PHONY: help clean test test-core test-provenance test-tools

help:
	@echo "Optional local maintenance commands"
	@echo "  make test   - run local repository checks"
	@echo "  make clean  - remove generated runtime/evidence artifacts"

clean:
	rm -rf __pycache__ .pytest_cache output/ traces/ checkpoints/ provenance/ evidence/
	@echo "Cleaned caches and generated research artifacts"

test: test-core test-provenance test-tools

test-core:
	python3 tests/test_all.py

test-provenance:
	python3 -m unittest tests.test_provenance -v

test-tools:
	python3 -m unittest tests.test_tool_cli tests.test_agent_plan -v
