.PHONY: help install install-dev test lint format type-check clean build publish docs

# Default target
help:
	@echo "Available commands:"
	@echo "  install      Install the package"
	@echo "  install-dev  Install development dependencies"
	@echo "  test         Run tests"
	@echo "  lint         Run linting checks"
	@echo "  format       Format code with black and isort"
	@echo "  type-check   Run type checking with mypy"
	@echo "  clean        Clean build artifacts"
	@echo "  build        Build distribution packages"
	@echo "  publish      Publish to PyPI"
	@echo "  docs         Generate documentation"

# Installation
install:
	pip install -e .

install-dev:
	pip install -e ".[dev,test]"

# Testing
test:
	pytest --cov=doc2mcp --cov-report=html --cov-report=term-missing

test-fast:
	pytest -x

# Code quality
lint:
	flake8 doc2mcp tests
	black --check doc2mcp tests
	isort --check-only doc2mcp tests

format:
	black doc2mcp tests
	isort doc2mcp tests

type-check:
	mypy doc2mcp

# Quality check (all)
check: lint type-check test

# Cleanup
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

# Building
build: clean
	python -m build

# Publishing
publish-test: build
	python -m twine upload --repository testpypi dist/*

publish: build
	python -m twine upload dist/*

# Documentation
docs:
	@echo "Documentation is in README.md and examples/"
	@echo "API docs are generated from docstrings"

# Development workflow
dev-setup: install-dev
	pre-commit install
	@echo "Development environment ready!"

# CI simulation
ci: clean install-dev lint type-check test
	@echo "All CI checks passed!"