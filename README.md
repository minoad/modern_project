# Project Setup

## Quick rundown

1. `mkdir src; mkdir src/<module_name>; touch src/<module_name>/__init__.py; touch src/<module_name>/py.typed;`
2. `mkdir src/tests;`
3. `touch .gitignore Makefile pyproject.toml requirements.txt requirements_dev.txt setup.cfg setup.py` Defaults below.
4. `python3.11 -m venv venv`
5. `source venv/bin/activate`
6. Add minimum code to `src/<module_name>/<module_name>.py`.
7. Add minimum code to `src/tests/test_<module_name>.py`.
8. Execute `pip install -e .`.  This installs the module in editable mode.  This way you can treat it as a standard import.  Editable means the code is symlinked to your current dev version.
9. Run `mypy src/`.

## Minimum File Content

* Minimum `src/<module_name>/<module_name>.py`

```python
from dataclasses import dataclass
@dataclass()
class Command:
    name: str
    def __post_init__(self):
        self.name = self.name.lower()
```

* Minimum `src/tests/<module_name>_test.py`

```python
from command.command import Command
def test_answer():
    assert "test" == Command(name="Test").name
```

* Minimum setup.cfg

```cfg
[metadata]
name = default_project
description = default
author = Micah Norman
license = MIT
platforms = linux, unix, osx, cygwin, win32

[options]
packages = command
install_requires = httpx
python_requires = >=3.11
package_dir = =src
zip_safe = no

[options.extras_require]
testing = 
    pytest
    pytest-cov
    mypy
    flake8
    tox

[options.package_data]
command = py.typed
```

* Minimum setup.py

```python
from setuptools import setup
if __name__ == "__main__":
    setup()
```

* Minimum requirements.txt

```txt
httpx
```

* Minimum pyproject.toml

```toml
[project]
name = "micah_python_project_generic"
version = "0.1"
description = ""
authors = [{ name = "Micah Norman", email = "minoad@gmail.com" }]
dependencies = ["pytest", "httpx", "fire", "pytest", "pipx", "hatch"]

[project.scripts]
cq_command = "command:main"

[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project.urls]
Source = "https://github.com/minoad/modern_project"

[tool.pytest.ini_options]
addopts = "--cov=command"
testpaths = [
    "test",
    "src/tests",
]

[tool.mypy]
mypy_path = "src"
check_untyped_defs = true
disallow_any_generics = true
ignore_missing_imports = true
no_implicit_optional = true
show_error_codes = true
strict_equality = true
warn_redundant_casts = true
warn_return_any = true
warn_unreachable = true
warn_unused_configs = true
no_implicit_reexport = true
pretty = true

```
