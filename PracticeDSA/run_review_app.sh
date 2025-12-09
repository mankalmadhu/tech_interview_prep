#!/bin/bash
# Script to run the Review Tracker App

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "uv is not installed. Please install uv first."
    exit 1
fi

echo "Starting Review Tracker..."
echo "If you are in VS Code, you can open the 'Simple Browser' command and navigate to http://localhost:8501"
echo "Starting Streamlit..."

# Run the app
cd "$(dirname "$0")" || exit
uv run python -m streamlit run review_app.py --server.headless true
