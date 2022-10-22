FROM python:3-alpine

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

# INSTALL DEPENDENCIES
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install -r requirements.txt

# COLLECTSTATIC
RUN python3 manage.py collectstatic --noinput

CMD gunicorn --bind 0.0.0.0:8000 \
             --workers 3 \
             --threads 2 \
             --keep-alive 5 \
             --max-requests 1000 \
             --worker-connections=1000 \
             --access-logfile - \
             --error-logfile - \
             --log-level critical \
             --worker-class gevent \
             --reload \
             --capture-output \
             api.wsgi:application
