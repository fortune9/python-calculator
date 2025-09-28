#!/bin/bash
set -e

echo "🚀 Setting up pre-commit hooks..."

# Install pre-commit
pip install pre-commit

# Install the hooks
pre-commit install

# Run on all files initially
pre-commit run --all-files

echo "✅ Pre-commit hooks installed successfully!"
echo "💡 The hooks will now run automatically on git commit."
