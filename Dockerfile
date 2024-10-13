FROM python:3.12-slim-bookworm

RUN pip install uv

WORKDIR /app

COPY django_play templates manage.py requirements.lock pyproject.toml ./
RUN uv pip install --no-cache --system -r requirements.lock

EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
