import os
import sys
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s] : %(message)s :")


project_name = "malaria"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/__init__.py",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/a_constants/__init__.py",
    f"src/{project_name}/b_entity/__init__.py",
    f"src/{project_name}/b_entity/config_entity.py",
    f"src/{project_name}/c_config/__init__.py",
    f"src/{project_name}/c_config/configuration.py",
    f"src/{project_name}/d_components/__init__.py",
    f"src/{project_name}/e_pipeline/__init__.py",
    f"src/{project_name}/f_utils/__init__.py",
    f"src/{project_name}/f_utils/common.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "main.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")
