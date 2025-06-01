# FastAPI URL Shortener

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
