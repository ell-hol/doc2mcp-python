# Contributing to doc2mcp Python SDK

Thank you for your interest in contributing to the doc2mcp Python SDK! This document provides guidelines for contributing to the project.

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip or poetry for dependency management
- Git

### Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/doc2mcp.git
   cd doc2mcp/python-sdk
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the package in development mode:
   ```bash
   pip install -e ".[dev]"
   ```

5. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Development Workflow

### Making Changes

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes following the coding standards below

3. Write or update tests for your changes

4. Run the test suite:
   ```bash
   pytest
   ```

5. Run code formatting and linting:
   ```bash
   black .
   flake8 .
   mypy doc2mcp
   ```

6. Commit your changes with a descriptive message:
   ```bash
   git commit -m "Add feature: your feature description"
   ```

7. Push to your fork and create a pull request

### Coding Standards

- Follow PEP 8 style guidelines
- Use Black for code formatting (line length: 88 characters)
- Use type hints for all function parameters and return values
- Write docstrings for all public functions and classes
- Keep functions focused and small
- Use meaningful variable and function names

### Code Organization

```
doc2mcp/
├── __init__.py          # Main exports
├── client.py            # Main client class
├── auth.py             # Authentication management
├── models.py           # Data models
├── exceptions.py       # Custom exceptions
├── cli.py              # Command-line interface
└── utils.py            # Utility functions
```

### Testing

- Write unit tests for all new functionality
- Use pytest for testing framework
- Mock external HTTP requests using `responses` library
- Aim for >90% test coverage
- Test both success and error scenarios

#### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=doc2mcp --cov-report=html

# Run specific test file
pytest tests/test_client.py

# Run specific test
pytest tests/test_client.py::TestDoc2MCPClient::test_upload_documents
```

### Documentation

- Update README.md if you add new features
- Add docstrings to all public methods
- Update API documentation for any changes
- Include examples in docstrings where helpful

## Pull Request Guidelines

### Before Submitting

- Ensure all tests pass
- Update documentation if needed
- Add yourself to contributors list if you haven't already
- Rebase your branch on the latest main branch

### PR Description Template

```markdown
## Description
Brief description of the changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tests pass locally
- [ ] Added new tests for new functionality
- [ ] Updated existing tests if needed

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review of code completed
- [ ] Documentation updated
- [ ] Changes generate no new warnings
```

### Review Process

1. Automated checks must pass (CI/CD pipeline)
2. At least one maintainer review required
3. Address all review feedback
4. Maintainer will merge when approved

## Reporting Issues

### Bug Reports

Include the following information:
- Python version
- doc2mcp SDK version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages and stack traces
- Minimal code example

### Feature Requests

- Describe the feature and its use case
- Explain why it would be valuable
- Consider implementation complexity
- Provide examples of the desired API

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Assume good intentions
- Follow the GitHub Community Guidelines

## Release Process

1. Update version in `pyproject.toml`
2. Update CHANGELOG.md
3. Create release PR
4. Tag release after merge
5. GitHub Actions will build and publish to PyPI

## Getting Help

- Check existing issues and documentation first
- Ask questions in GitHub Discussions
- Join our community chat (if available)
- Tag maintainers in issues if urgent

## Recognition

Contributors will be:
- Added to the contributors list
- Mentioned in release notes for significant contributions
- Invited to join the maintainer team for consistent contributors

Thank you for contributing to doc2mcp!