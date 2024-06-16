from typing import Literal


class TemplateLoader:
    @classmethod
    def get_pyproject_toml_template(cls, option: Literal["base"] = "base"):
        from .pyproject_toml import templates
        return templates["base"]

    @classmethod
    def get_setup_env_template(cls, option: Literal["base"] = "base"):
        from .setup_env_sh import templates
        return templates["base"]
