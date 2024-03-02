set export

PORT := "8000"
APPLICATION_NAME := "django-play"
POSTGRES_PORT := "5432"
POSTGRES_NAME := "postgres"
POSTGRES_USER := "postgres"
POSTGRES_PASSWORD := "pass"

default: start

run:
    just export-requirements
    docker-compose -f docker/docker-compose.services.yml -f docker/docker-compose.app.yml up --build -d

tear:
    docker-compose down

start:
    #!/bin/zsh

    python manage.py migrate
    python manage.py runserver 0.0.0.0:${PORT=8000}

setup-dev-env:
    zsh scripts/setup-dev-env.zsh

[private]
export-requirements:
    . .venv/bin/activate
    poetry export --without-hashes --format=requirements.txt > requirements.txt
