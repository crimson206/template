# region

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
\[discussion_block\]
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


template = add_options(
    template,
    options=Options(
        discussion=False
    )
)

name_space = "None",
module_name = "None",
description = "None",



pyproject_body = format_insert(
    template,
    kwargs=Kwargs(
        name_space=name_space,
        module_name=module_name,
        description=description,
    )
)
