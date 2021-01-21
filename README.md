# Project

Description.

## Getting started

### Install Python

```sh
$ pyenv install 3.9.1
```

### Install dependencies

```sh
$ poetry install
```

### Set up database

```sh
$ poetry run python manage.py migrate
$ poetry run python manage.py createsuperuser
```

### Run server

```sh
$ poetry run python manage.py runserver
```
