set export

PORT := "8000"
APPLICATION_NAME := "django-play"
POSTGRES_PORT := "5432"
POSTGRES_NAME := "django_play_db"
POSTGRES_USER := "django-play-user"
POSTGRES_PASSWORD := "secure-password"
COMPOSE_FILES := "-f docker-compose.yml -f docker/docker-compose.services.yml"

default: run-dev

run:
    docker compose $COMPOSE_FILES up --build -d

build:
    docker build -t django-play .

tear:
    docker compose $COMPOSE_FILES down

start:
    #!/bin/zsh

    python manage.py runserver 0.0.0.0:$PORT

run-dev: install-modules run-db-migrations
    #!/bin/zsh

    . .venv/bin/activate
    python manage.py runserver 0.0.0.0:$PORT

run-db-migrations:
    #!/bin/zsh

    . .venv/bin/activate
    python manage.py migrate

lint:
    #!/bin/zsh

    . .venv/bin/activate
    ruff check .

lint-fix:
    #!/bin/zsh

    . .venv/bin/activate
    ruff check . --fix

format:
    #!/bin/zsh

    . .venv/bin/activate
    ruff format .

post-dev-container-create:
    just .devcontainer/post-create
    just bootstrap

# Bootstrap project
bootstrap: install-modules setup-pre-commit

[private]
install-modules:
    #!/bin/zsh

    . "$HOME/.rye/env"

    rye sync

[private]
setup-pre-commit:
    #!/bin/zsh

    . .venv/bin/activate
    pre-commit install
