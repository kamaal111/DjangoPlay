set export

PORT := "8000"
APPLICATION_NAME := "django-play"

default: build run

build:
    docker build -t $APPLICATION_NAME .

run:
    docker rm $APPLICATION_NAME || true
    docker run -dp $PORT:$PORT --name $APPLICATION_NAME -e PORT=$PORT $APPLICATION_NAME

run-dev:
    python manage.py migrate
    python manage.py runserver 8000
