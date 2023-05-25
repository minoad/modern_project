# Project Management/Setup, Tools and Testing

## Project Management

* [pyproject.toml](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/)
* [setup.py](https://pip.pypa.io/en/stable/reference/build-system/setup-py/)

* poetry
* hatch

## Virtual Environment

```shell
# python<version> -m venv venv
python3.11 -m venv venv 
```

## Dependency Management

* tox
* pipx
* pip

To make packages installable, need pyproject.toml at the top level.

## Linting

* black
* mypy
* flake8

## Testing

* pytest
* tox


### Github Actions



## Config files

* pyproject.toml
* setup.cfg
* setup.py
  * Old method.  Can still be required especially for editable mode.  Simply put the following:

```python
from setuptools import setup

if __name__ == "__main__":
    setup()
```