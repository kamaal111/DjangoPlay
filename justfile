set export

PORT := "8000"
APPLICATION_NAME := "django-play"
POSTGRES_PORT := "5432"
POSTGRES_NAME := "django_play_db"
POSTGRES_USER := "django-play-user"
POSTGRES_PASSWORD := "secure-password"

default: start

run:
    just export-requirements
    docker-compose -f docker/docker-compose.services.yml -f docker/docker-compose.app.yml up --build -d

tear:
    docker-compose down

start: install-modules run-db-migrations
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

[private]
export-requirements:
    . .venv/bin/activate
    poetry export --without-hashes --format=requirements.txt > requirements.txt
