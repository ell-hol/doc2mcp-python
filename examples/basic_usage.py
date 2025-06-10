#!/usr/bin/env python3
"""
Basic usage example for the doc2mcp Python SDK
"""

import sys
import os
from pathlib import Path

# Add the SDK to the path for testing
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from doc2mcp import Doc2MCPClient, Doc2MCPError


def main():
    # Initialize client (assuming local development server)
    client = Doc2MCPClient("http://localhost:5000")
    
    try:
        print("🚀 doc2mcp Python SDK Example")
        print("=" * 40)
        
        # List existing projects
        print("\n📁 Existing projects:")
        projects = client.get_projects()
        if projects:
            for project in projects:
                print(f"  • {project.name} (ID: {project.id}, Status: {project.status.value})")
        else:
            print("  No projects found")
        
        # Create sample documentation files for testing
        test_dir = Path("test_docs")
        test_dir.mkdir(exist_ok=True)
        
        # Create a sample markdown file
        sample_md = test_dir / "sample_api.md"
        sample_md.write_text("""# Sample API Documentation

## Authentication
All API requests require an API key in the header:
```
Authorization: Bearer your-api-key
```

## Endpoints

### GET /users
Retrieve all users in the system.

**Response:**
```json
{
  "users": [
    {"id": 1, "name": "John Doe", "email": "john@example.com"}
  ]
}
```

### POST /users
Create a new user.

**Request Body:**
```json
{
  "name": "Jane Smith",
  "email": "jane@example.com"
}
```
""")
        
        # Create another sample file
        sample_guide = test_dir / "getting_started.md"
        sample_guide.write_text("""# Getting Started Guide

## Installation
Install the SDK using pip:
```bash
pip install our-sdk
```

## Quick Start
1. Import the SDK
2. Initialize the client
3. Make your first API call

## Configuration
Set your environment variables:
- `API_KEY`: Your API key
- `API_URL`: The API base URL

## Troubleshooting
Common issues and solutions:
- Authentication errors: Check your API key
- Rate limits: Implement exponential backoff
""")
        
        print(f"\n📤 Uploading documentation...")
        
        # Upload the test files
        project = client.upload_documents(
            name="SDK Example Project",
            files=[str(sample_md), str(sample_guide)],
            description="Example project created by the Python SDK"
        )
        
        print(f"✅ Project created successfully!")
        print(f"   Name: {project.name}")
        print(f"   ID: {project.id}")
        print(f"   Slug: {project.slug}")
        print(f"   Status: {project.status.value}")
        print(f"   Files: {project.file_count}")
        print(f"   MCP Endpoint: {client.get_mcp_endpoint(project.slug)}")
        
        # Wait a moment for processing
        print(f"\n⏳ Waiting for processing to complete...")
        import time
        time.sleep(3)
        
        # Search the documentation
        print(f"\n🔍 Searching for 'authentication'...")
        results = client.search(project.slug, "authentication", project.api_token)
        
        if results.chunks:
            print(f"   Found {len(results.chunks)} results:")
            for i, chunk in enumerate(results.chunks, 1):
                source = chunk.metadata.get('source', 'Unknown')
                content_preview = chunk.content[:100].replace('\n', ' ')
                print(f"   {i}. {source}: {content_preview}...")
        else:
            print("   No results found")
        
        # Search for another term
        print(f"\n🔍 Searching for 'installation'...")
        results = client.search(project.slug, "installation", project.api_token)
        
        if results.chunks:
            print(f"   Found {len(results.chunks)} results:")
            for i, chunk in enumerate(results.chunks, 1):
                source = chunk.metadata.get('source', 'Unknown')
                content_preview = chunk.content[:100].replace('\n', ' ')
                print(f"   {i}. {source}: {content_preview}...")
        else:
            print("   No results found")
        
        print(f"\n📊 Final project list:")
        updated_projects = client.get_projects()
        for project in updated_projects:
            print(f"  • {project.name} (ID: {project.id}, Status: {project.status.value})")
        
        print(f"\n🎉 Example completed successfully!")
        print(f"   MCP Endpoint: {client.get_mcp_endpoint(project.slug)}")
        print(f"   You can now use this endpoint with Claude or other AI assistants")
        
        # Clean up test files
        sample_md.unlink()
        sample_guide.unlink()
        test_dir.rmdir()
        
    except Doc2MCPError as e:
        print(f"❌ Error: {e}")
        return 1
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())