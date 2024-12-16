import sys
import os

# Add the project directory and virtual environment site-packages to Python path
project_dir = '/var/www/html/ictazNotice'
venv_site_packages = '/var/www/html/ictazNotice/venv/lib/python3.6/site-packages'

sys.path.insert(0, project_dir)
sys.path.insert(1, venv_site_packages)

# Import your Flask app
from app import app as application
