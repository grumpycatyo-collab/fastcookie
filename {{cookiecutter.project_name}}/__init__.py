"""{{cookiecutter.project_name}} package."""

from pathlib import Path

with open(Path(__file__).parent / "VERSION") as version_file:
    __version__ = version_file.read().strip()
