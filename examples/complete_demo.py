#!/usr/bin/env python3
"""
Complete demonstration of the doc2mcp Python SDK functionality
"""

import sys
import os
import time
from pathlib import Path

# Add the SDK to the path for testing
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from doc2mcp import Doc2MCPClient, Doc2MCPError, ProjectStatus


def create_sample_docs():
    """Create comprehensive sample documentation"""
    docs_dir = Path("demo_docs")
    docs_dir.mkdir(exist_ok=True)
    
    # API Reference
    (docs_dir / "api.md").write_text("""# API Reference

## Authentication
All requests require an API key in the Authorization header:
```
Authorization: Bearer sk-your-api-key-here
```

## Base URL
```
https://api.example.com/v1
```

## Rate Limits
- 1000 requests per hour per API key
- 10 requests per second burst limit

## Endpoints

### Users
- `GET /users` - List all users
- `POST /users` - Create a new user
- `GET /users/{id}` - Get user by ID
- `PUT /users/{id}` - Update user
- `DELETE /users/{id}` - Delete user

### Projects
- `GET /projects` - List projects
- `POST /projects` - Create project
- `GET /projects/{id}` - Get project details

## Error Codes
- 400: Bad Request - Invalid parameters
- 401: Unauthorized - Invalid API key
- 403: Forbidden - Insufficient permissions
- 404: Not Found - Resource doesn't exist
- 429: Too Many Requests - Rate limit exceeded
- 500: Internal Server Error
""")
    
    # Installation Guide
    (docs_dir / "installation.md").write_text("""# Installation Guide

## Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

## Install via pip
```bash
pip install our-sdk
```

## Install from source
```bash
git clone https://github.com/example/sdk.git
cd sdk
pip install -e .
```

## Verify Installation
```python
import our_sdk
print(our_sdk.__version__)
```

## Configuration
Create a `.env` file in your project root:
```
API_KEY=your-api-key-here
API_URL=https://api.example.com/v1
```

## Environment Variables
- `API_KEY`: Your API authentication key
- `API_URL`: The base API URL (optional)
- `DEBUG`: Enable debug logging (optional)
""")
    
    # Quick Start
    (docs_dir / "quickstart.md").write_text("""# Quick Start Guide

## Basic Usage
```python
from our_sdk import Client

# Initialize client
client = Client(api_key="your-key")

# Create a user
user = client.users.create({
    "name": "John Doe",
    "email": "john@example.com"
})

# List all users
users = client.users.list()

# Get specific user
user = client.users.get(user_id=123)
```

## Error Handling
```python
try:
    user = client.users.get(999)
except UserNotFound:
    print("User not found")
except APIError as e:
    print(f"API error: {e}")
```

## Pagination
```python
# Get first page
users = client.users.list(page=1, limit=50)

# Iterate through all pages
for user in client.users.list_all():
    print(user.name)
```

## Async Usage
```python
import asyncio
from our_sdk import AsyncClient

async def main():
    client = AsyncClient(api_key="your-key")
    users = await client.users.list()
    await client.close()

asyncio.run(main())
```
""")
    
    # Troubleshooting
    (docs_dir / "troubleshooting.md").write_text("""# Troubleshooting

## Common Issues

### Authentication Errors
**Problem**: Getting 401 Unauthorized errors
**Solution**: 
- Verify your API key is correct
- Check that the key hasn't expired
- Ensure proper Authorization header format

### Rate Limiting
**Problem**: 429 Too Many Requests errors
**Solution**:
- Implement exponential backoff
- Reduce request frequency
- Consider upgrading your plan

### Connection Issues
**Problem**: Network timeouts or connection errors
**Solution**:
- Check your internet connection
- Verify the API URL is correct
- Try increasing timeout values

### SSL Certificate Errors
**Problem**: SSL verification failures
**Solution**:
```python
# For testing only - not recommended for production
client = Client(api_key="key", verify_ssl=False)
```

## Debug Mode
Enable debug logging to troubleshoot issues:
```python
import logging
logging.basicConfig(level=logging.DEBUG)

client = Client(api_key="key", debug=True)
```

## Getting Help
- Check our FAQ at https://example.com/faq
- Submit issues at https://github.com/example/sdk/issues
- Contact support at support@example.com
""")
    
    return docs_dir


def main():
    print("doc2mcp Python SDK - Complete Demo")
    print("=" * 50)
    
    # Initialize client
    client = Doc2MCPClient("http://localhost:5000")
    
    try:
        # Create sample documentation
        print("\n1. Creating sample documentation...")
        docs_dir = create_sample_docs()
        doc_files = list(docs_dir.glob("*.md"))
        print(f"   Created {len(doc_files)} documentation files")
        
        # Upload documentation
        print("\n2. Uploading documentation to doc2mcp...")
        project = client.upload_documents(
            name="Complete SDK Documentation",
            files=[str(f) for f in doc_files],
            description="Comprehensive SDK documentation with API reference, installation guide, and troubleshooting"
        )
        
        print(f"   Project created: {project.name}")
        print(f"   ID: {project.id}")
        print(f"   Slug: {project.slug}")
        print(f"   Status: {project.status.value}")
        print(f"   Files: {project.file_count}")
        
        # Wait for processing
        print("\n3. Waiting for document processing...")
        max_wait = 30  # seconds
        start_time = time.time()
        
        while project.status == ProjectStatus.PROCESSING and (time.time() - start_time) < max_wait:
            time.sleep(2)
            updated_project = client.get_project(project.id)
            project.status = updated_project.status
            print(f"   Status: {project.status.value}")
        
        if project.status == ProjectStatus.READY:
            print("   Processing complete!")
        else:
            print("   Processing still in progress...")
        
        # Demonstrate search functionality
        print("\n4. Testing search functionality...")
        
        search_queries = [
            "authentication",
            "installation", 
            "rate limits",
            "error handling",
            "troubleshooting"
        ]
        
        for query in search_queries:
            print(f"\n   Searching for '{query}':")
            try:
                results = client.search(project.slug, query, limit=3)
                if results.chunks:
                    for i, chunk in enumerate(results.chunks, 1):
                        source = chunk.metadata.get('source', 'Unknown')
                        preview = chunk.content[:80].replace('\n', ' ').strip()
                        print(f"     {i}. {source}: {preview}...")
                else:
                    print("     No results found")
            except Exception as e:
                print(f"     Error: {e}")
        
        # Show MCP endpoint information
        print(f"\n5. MCP Integration Details:")
        mcp_url = client.get_mcp_endpoint(project.slug)
        print(f"   Endpoint URL: {mcp_url}")
        print(f"   Usage with Claude: Add this URL as an MCP server")
        print(f"   Direct API access: GET {mcp_url}?q=your-search-query")
        
        # Demonstrate project management
        print(f"\n6. Project Management:")
        all_projects = client.get_projects()
        print(f"   Total projects on server: {len(all_projects)}")
        
        for proj in all_projects:
            print(f"   • {proj.name} (ID: {proj.id}, Status: {proj.status.value})")
        
        print(f"\n7. Complete Demo Results:")
        print(f"   ✓ Successfully uploaded {project.file_count} files")
        print(f"   ✓ Generated MCP-compliant search endpoint")
        print(f"   ✓ Tested semantic search across documentation")
        print(f"   ✓ Ready for AI assistant integration")
        
        print(f"\nNext Steps:")
        print(f"   • Copy the MCP endpoint URL: {mcp_url}")
        print(f"   • Configure Claude or GPT to use this endpoint")
        print(f"   • Ask questions about your documentation")
        print(f"   • The AI will automatically search and find relevant content")
        
        return 0
        
    except Doc2MCPError as e:
        print(f"   Error: {e}")
        return 1
        
    except Exception as e:
        print(f"   Unexpected error: {e}")
        return 1
        
    finally:
        # Cleanup
        if 'docs_dir' in locals():
            for file in docs_dir.glob("*"):
                file.unlink()
            docs_dir.rmdir()


if __name__ == "__main__":
    sys.exit(main())