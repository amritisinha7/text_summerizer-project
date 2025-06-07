import os
from pathlib import Path  # ✅ Corrected import

import logging

# ✅ Fixed logging format (missing closing bracket and colon)
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s:')

project_name = "textsummerizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",  # ✅ Fixed typo (__init__py -> __init__.py)
    f"src/{project_name}/utils/common.py",    # ✅ Corrected path name from "_utils"
    f"src/{project_name}/logging/__init__.py",  # ✅ Fixed double slashes
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",  # ✅ Fixed spelling: congig -> config
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)  # ✅ Use Path from pathlib
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # ✅ Fixed keyword: exit_ok -> exist_ok
        logging.info(f"Creating directory: {filedir} for the file {filename}")  # ✅ Fixed var name: filder -> filedir

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass  # Creates empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
