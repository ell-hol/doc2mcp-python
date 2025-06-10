# Changelog

All notable changes to the doc2mcp Python SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial release of the doc2mcp Python SDK
- Core client functionality for interacting with doc2mcp service
- Authentication management with persistent credential storage
- Command-line interface (CLI) for easy project management
- Support for uploading documentation files
- Project listing and management
- Document search functionality via MCP endpoints
- Comprehensive error handling and custom exceptions
- Type hints throughout the codebase
- Full test coverage with pytest
- CI/CD pipeline with GitHub Actions
- Documentation and examples

### Features
- **Client Class**: Main interface for SDK operations
- **Authentication**: Login/logout functionality similar to wandb
- **CLI Commands**: 
  - `doc2mcp login` - Authenticate with server
  - `doc2mcp logout` - Clear stored credentials
  - `doc2mcp whoami` - Show current login status
  - `doc2mcp upload` - Upload documentation files
  - `doc2mcp list` - List all projects
  - `doc2mcp search` - Search project documents
  - `doc2mcp delete` - Delete projects
- **Project Management**: Create, list, and delete documentation projects
- **Document Search**: Semantic search through uploaded documentation
- **MCP Integration**: Full compatibility with Model Context Protocol

### Developer Features
- Type safety with comprehensive type hints
- Async/await support for non-blocking operations
- Extensible architecture for future enhancements
- Mock-friendly design for testing
- Comprehensive logging and debugging support

## [1.0.0] - 2024-12-XX

### Added
- Initial stable release
- Production-ready SDK for doc2mcp service
- Complete CLI interface
- Full documentation and examples
- CI/CD pipeline and automated testing

### Security
- Secure credential storage
- API token authentication
- Input validation and sanitization
- Protection against common vulnerabilities