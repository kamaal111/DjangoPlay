FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONFAULTHANDLER=1
ENV PYTHONHASHSEED=random
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100

WORKDIR /code

COPY django_play templates manage.py requirements.txt start.sh /code/

RUN python -m venv .venv
RUN . .venv/bin/activate
RUN pip install -r requirements.txt

EXPOSE ${PORT}
CMD ["sh", "start.sh"]
