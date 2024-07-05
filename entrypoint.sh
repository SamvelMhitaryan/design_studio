#!/bin/bash
python3 manage.py collectstatic --no-input
python3 manage.py migrate


gunicorn design.wsgi:application --bind 0.0.0.:8002 