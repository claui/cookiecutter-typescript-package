"""End-to-end test"""

import subprocess
from tempfile import mkdtemp

from cookiecutter.main import cookiecutter
from .settings import PROJECT_ROOT


def run() -> None:
    """Runs the end-to-end test."""
    target_path_name = cookiecutter(
        str(PROJECT_ROOT),
        no_input=True,
        output_dir=mkdtemp(suffix=".e2e", prefix="cookiecutter."),
        extra_context={
            "project_slug": "flubber",
            "project_license": "Proprietary",
        },
    )
    print(target_path_name)
    subprocess.run("yarn lint", check=True, cwd=target_path_name, shell=True)
    subprocess.run("yarn compile", check=True, cwd=target_path_name, shell=True)
    subprocess.run("yarn test", check=True, cwd=target_path_name, shell=True)
