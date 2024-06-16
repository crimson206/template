templates = {}

templates['base'] = r'''[build-system]
requires = ["setuptools>=61.0.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "\[name_space\]-\[module_name\]"
version = "0.1.0"
description = "\[description\]"
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

[tool.setuptools.entry-points.console_scripts]
hello = "\[name_space\]-\[module_name\].\[module_name\]:main"

[project.urls]
"Homepage" = "https://github.com/\[github_id\]/\[module_name\]"
"Bug Tracker" = "https://github.com/\[github_id\]/\[module_name\]/issues"
"Discussion" = "https://github.com/\[github_id\]/\[module_name\]/discussions"
'''