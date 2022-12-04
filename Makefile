#!/bin/bash
.PHONY: default
.SILENT:


default:

build:
	docker-compose build --force-rm --no-cache --pull

start:
	docker-compose up -d

stop:
	docker-compose stop

down:
	docker-compose down --volumes

bash:
	docker-compose exec web bash

shell:
	docker-compose exec web python manage.py shell

loaddata:
	docker-compose exec web python manage.py loaddata warframes news items sellitems products

migrate:
	docker-compose exec web python manage.py migrate --noinput

migrations:
	docker-compose exec web python manage.py makemigrations $(app)

collectstatic:
	docker-compose exec web python manage.py collectstatic --noinput

createsuperuser:
	docker-compose exec web python manage.py createsuperuser $(args)

manage:
	docker-compose exec web python manage.py $(args)

# Code Quality
# -----------------------------------------------------------------------------
_isort:
	docker-compose exec web isort --diff --check-only .

_black:
	docker-compose exec web black --check .

_mypy:
	docker-compose exec web mypy . --exclude migrations

_isort-clear:
	docker-compose exec web isort .

_black_fix:
	docker-compose exec web black .

lint: _isort _black _mypy
format-code: _isort-clear _black_fix
