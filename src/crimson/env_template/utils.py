# region Pre-Defined

import os
from typing import Literal
from .format_template import TemplateLoader
from crimson.templator import format_insert
import subprocess
from .config import (
    name,
    email,
    github_id,
    name_space,
    module_name,
    description,
)


def create_skeleton():
    os.makedirs(f"src/{name_space}/{module_name}", exist_ok=True)
    with open(f"src/{name_space}/{module_name}/__init__.py", "w") as f:
        f.write("# Init file for the module")


def generate_setup_env_script(option: Literal['base'] = "base"):

    template = TemplateLoader.get_setup_env_template(option)

    with open("scripts/setup_env.sh", "w") as file:
        script = format_insert(
            template, module_name=module_name, bin_bash="# !bin/bash"
        )
        file.write(script)

    print(
        f"Now, you can access the module name {module_name} in your terminal by $MODULE_NAME"
    )
    print("To generate an conda env for your new module, run following command.")
    print("source scripts/setup_env.sh")


def generate_toml(option: Literal['base'] = "base"):

    template = TemplateLoader.get_pyproject_toml_template(option)

    pyproject_body: str = format_insert(
        template,
        name=name,
        email=email,
        github_id=github_id,
        name_space=name_space,
        module_name=module_name,
        description=description,
    )

    with open("pyproject_test.toml", "w") as file:
        file.write(pyproject_body)


def setup_env():
    subprocess.run(["bash", "-c", "source scripts/setup_env.sh"], check=True)
