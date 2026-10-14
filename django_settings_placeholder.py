"""Django settings placeholder for Art Magic Studio."""
import os

# Read token from .env or environment variable
API_TOKEN = os.getenv('API_TOKEN')

if not API_TOKEN:
    raise ValueError("API_TOKEN is not set in environment or .env file.")

# Project name (for future Django integration)
PROJECT_NAME = "artmagic_studio"

# PythonAnywhere specific: ensure token is available in web app
# (Add API_TOKEN=78f42f42a... in PythonAnywhere Web > Variables)