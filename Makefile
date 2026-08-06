.PHONY: clean test

clean:
	rm -rf __pycache__ .pytest_cache output/
	@echo "Cleaned caches and generated artifacts"

test:
	python3 tests/test_all.py
