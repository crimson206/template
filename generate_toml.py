# region Pre-Defined


from pydantic import BaseModel
from crimson.templator import format_insert

template = r'''[build-system]
requires = ["setuptools>=61.0.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "\[name_space\]-\[module_name\]"
version = "0.1.0"
description = \[description\]
readme = "README.md"
authors = [
  { name="\[name\]", email="\[email\]" },
]

classifiers = [
    "Programming Language :: Python :: 3",

    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",

    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = [
    "pydantic",
]
requires-python = ">=3.9"

[project.urls]
"Homepage" = "https://github.com/\[github_id\]/\[module_name\]"
"Bug Tracker" = "https://github.com/\[github_id\]/\[module_name\]/issues"
'''


class Kwargs(BaseModel):
    name: str = "Sisung Kim"
    email: str = "sisung.kim1@gmail.com"
    github_id: str = "crimson206"
    name_space: str
    module_name: str
    description: str


class Options(BaseModel):
    discussion: bool = False


def add_options(template: str, options: Options) -> str:

    if options.discussion:
        discussion_block = r'''"Discussion" = "https://github.com/\[github_id\]/\[module_name\]/discussions"'''
        template += discussion_block

    return template

# endregion


# ******************************************************
# region User Setup


options = Options(
    # Will you use the discussion session in your repo?
    discussion=False
)

# Define the general information of your package
kwargs = Kwargs(
    name_space="None",
    module_name="None",
    description="None",
)

# endregion

# ******************************************************
# region Execution

template: str = add_options(
    template,
    options=options
)

pyproject_body: str = format_insert(
    template,
    **kwargs.model_dump()
)

with open('pyproject.toml', "w") as file:
    file.write(pyproject_body)

# endregion
