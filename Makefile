.PHONY: clean test test-core test-provenance

clean:
	rm -rf __pycache__ .pytest_cache output/ traces/ checkpoints/ provenance/
	@echo "Cleaned caches and generated artifacts"

test: test-core test-provenance

test-core:
	python3 tests/test_all.py

test-provenance:
	python3 -m unittest tests.test_provenance -v
