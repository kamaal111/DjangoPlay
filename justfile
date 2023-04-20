set export

PORT := "8000"
APPLICATION_NAME := "django-play"

default: export-requirements build run

export-requirements:
    poetry export --without-hashes --format=requirements.txt > requirements.txt

build:
    docker build -t $APPLICATION_NAME .

run:
    docker stop $APPLICATION_NAME || true
    docker rm $APPLICATION_NAME || true
    docker run -dp $PORT:$PORT --name $APPLICATION_NAME -e PORT=$PORT \
        --volume $(pwd):/code $APPLICATION_NAME

tear:
    docker stop $APPLICATION_NAME

run-dev:
    python manage.py migrate
    python manage.py runserver 8000
