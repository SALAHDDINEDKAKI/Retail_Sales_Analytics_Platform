# Run this once per new project (Windows PowerShell):
#   .\setup.ps1
#
# If you get an execution policy error, run this first (once, ever):
#   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

Write-Host "Creating virtual environment in .venv ..."
python -m venv .venv

Write-Host "Activating virtual environment ..."
.\.venv\Scripts\Activate.ps1

Write-Host "Installing requirements ..."
pip install -r requirements.txt

Write-Host "Registering Jupyter kernel for this project ..."
python -m ipykernel install --user --name project-venv --display-name "Python (this project)"

Write-Host ""
Write-Host "Done. In VS Code: Ctrl+Shift+P -> 'Python: Select Interpreter' -> choose .venv"
Write-Host "Next: copy .env.example to .env and fill in your DB password."
