#!/usr/bin/env python3
"""
Command-line interface example for the doc2mcp Python SDK
"""

import sys
import os
from pathlib import Path

# Add the SDK to the path for testing
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from doc2mcp.cli import main


def test_cli():
    """Test the CLI interface"""
    print("🚀 Testing doc2mcp CLI")
    print("=" * 30)
    
    # Create test documentation
    test_dir = Path("cli_test_docs")
    test_dir.mkdir(exist_ok=True)
    
    readme = test_dir / "README.md"
    readme.write_text("""# Test Project

This is a test project for the doc2mcp CLI.

## Features
- Easy documentation upload
- Instant MCP endpoints
- AI-ready search

## Usage
Simply upload your docs and get MCP endpoints.
""")
    
    api_doc = test_dir / "api.md"
    api_doc.write_text("""# API Reference

## Authentication
Use Bearer tokens for authentication.

## Rate Limits
- 1000 requests per hour
- 10 requests per second

## Error Codes
- 401: Unauthorized
- 429: Rate limit exceeded
- 500: Server error
""")
    
    try:
        # Test upload command
        print("\n📤 Testing upload command...")
        sys.argv = [
            'doc2mcp',
            'upload',
            'CLI Test Project',
            '--directory', str(test_dir),
            '--description', 'Testing the CLI upload functionality'
        ]
        
        result = main()
        if result == 0:
            print("✅ Upload command successful")
        else:
            print("❌ Upload command failed")
            return 1
        
        print("\n📋 Testing list command...")
        sys.argv = ['doc2mcp', 'list']
        result = main()
        if result == 0:
            print("✅ List command successful")
        else:
            print("❌ List command failed")
            return 1
        
        print("\n🔍 Testing search command...")
        sys.argv = [
            'doc2mcp', 
            'search', 
            'cli-test-project',
            'authentication',
            '--limit', '5'
        ]
        result = main()
        if result == 0:
            print("✅ Search command successful")
        else:
            print("❌ Search command failed")
            return 1
        
        print("\n🎉 All CLI tests passed!")
        
    finally:
        # Clean up
        for file in test_dir.glob("*"):
            file.unlink()
        test_dir.rmdir()
    
    return 0


if __name__ == "__main__":
    sys.exit(test_cli())