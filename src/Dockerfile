FROM python:3.11.0-alpine

LABEL maintainer="yurinogueira@id.uff.br"
LABEL vendor="Yuri Nogueira"

# PYTHON ENV
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONHASHSEED random
ENV PYTHONBREAKPOINT ipdb.set_trace

# PIP ENV
ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on
ENV PIP_DEFAULT_TIMEOUT 100

# DJANGO ENV
ENV DJANGO_SETTINGS_MODULE api.settings
ENV TZ America/Sao_Paulo

# SET UP WORKDIR
WORKDIR /usr/src/app
COPY ./ /usr/src/app

RUN apk update && \
    apk add --virtual build-deps gcc musl-dev && \
    apk add postgresql-dev

# INSTALL DEPENDENCIES
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:8000 \
             --reload \
             --workers 3 \
             --timeout 60 \
             --log-level=debug \
             --capture-output \
             api.wsgi:application
