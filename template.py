import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger("template")

project_name = "mlops"

base_path = Path(f"src/{project_name}")

list_of_files = [
    ".github/workflows/.gitkeep",
    base_path / "__init__.py",
    base_path / "components" / "__init__.py",
    base_path / "utils" / "__init__.py",
    base_path / "utils" / "common.py",
    base_path / "config" / "__init__.py",
    base_path / "config" / "configuration.py",
    base_path / "pipeline" / "__init__.py",
    base_path / "entity" / "__init__.py",
    base_path / "entity" / "config_entity.py",
    base_path / "constants" / "__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent

    if filedir != Path():
        filedir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath.name} already exists")
