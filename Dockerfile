FROM python:3.11

ARG YOUR_ENV

ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.4.0

RUN pip install "poetry==$POETRY_VERSION"
RUN apt-get -y install git

WORKDIR /test
COPY poetry.lock pyproject.toml /test/

RUN poetry config virtualenvs.create false \
  && poetry install --no-root --no-interaction --no-ansi

COPY . /test

RUN adduser --disabled-password docker-admin

USER docker-admin 


