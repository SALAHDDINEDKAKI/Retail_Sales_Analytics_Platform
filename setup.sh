#!/usr/bin/env bash
# Run this once per new project (Mac/Linux):
#   bash setup.sh

set -e

echo "Creating virtual environment in .venv ..."
python3 -m venv .venv

echo "Activating virtual environment ..."
source .venv/bin/activate

echo "Installing requirements ..."
pip install -r requirements.txt

echo "Registering Jupyter kernel for this project ..."
python -m ipykernel install --user --name project-venv --display-name "Python (this project)"

echo ""
echo "Done. In VS Code: Cmd+Shift+P -> 'Python: Select Interpreter' -> choose .venv"
echo "Next: copy .env.example to .env and fill in your DB password."
