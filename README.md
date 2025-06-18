# FastAPI URL Shortener

[![Python checks 🐍](https://img.shields.io/github/actions/workflow/status/mahenzon/fastapi-url-shortener/python-checks.yaml?branch=master&label=Python%20checks%20%F0%9F%90%8D&logo=github&style=for-the-badge)](https://github.com/mahenzon/fastapi-url-shortener/actions/workflows/python-checks.yaml)
[![Python Version](https://img.shields.io/badge/python-3.13%2B-blue?logo=python&style=for-the-badge)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?logo=python&style=for-the-badge)](https://github.com/psf/black)
[![Lint: Ruff](https://img.shields.io/badge/lint-ruff-%23efc000?logo=ruff&logoColor=white&style=for-the-badge)](https://github.com/astral-sh/ruff)
[![Type Checking: mypy](https://img.shields.io/badge/type%20checking-mypy-blueviolet?logo=python&style=for-the-badge)](https://github.com/python/mypy)
[![Dependency: uv](https://img.shields.io/badge/dependencies-uv-4B8BBE?logo=python&style=for-the-badge)](https://github.com/astral-sh/uv)

## Develop

Check GitHub Actions after any push.


### Setup

Right click `url-shortener` -> Mark Directory as -> Sources Root


### Install depencies

Install all packages:
```shell
uv sync
```

### Configure pre-commit

Install pre-commit hook:
```shell
pre-commit install
```

### Run

Go to workdir:
```shell
cd url-shortener
```

Run dev server:
```shell
fastapi dev
```

## Snippets

```shell
python -c 'import secrets;print(secrets.token_urlsafe(16))'
```
