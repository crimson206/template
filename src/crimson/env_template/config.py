import os
import subprocess

subprocess.run(["bash", "-c", "source config.sh"], check=True)

name = os.getenv("NAME"),
email = os.getenv("EMAIL"),
github_id = os.getenv("GITHUB_ID"),
name_space = os.getenv("NAME_SPACE"),
module_name = os.getenv("MODULE_NAME"),
description = os.getenv("DESCRIPTION"),

if module_name == "env_template":
    raise "set your config.sh first."
