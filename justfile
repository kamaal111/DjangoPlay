set export

PORT := "8000"
APPLICATION_NAME := "django-play"

default: export-requirements run

export-requirements:
    poetry export --without-hashes --format=requirements.txt > requirements.txt

run:
    docker-compose up --build -d

tear:
    docker-compose down

run-dev:
    python manage.py migrate
    python manage.py runserver $PORT
