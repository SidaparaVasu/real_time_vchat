#!/usr/bin/env bash
# exit on error
# set -o errexit

# pip install -r requirements.txt

# pip install gunicorn

# set DJANGO_SETTINGS_MODULE = real_time_chatapp.settings

# gunicorn --env DJANGO_SETTINGS_MODULE=real_time_chatapp.settings real_time_chatapp.asgi

# python manage.py collectstatic --no-input
# python manage.py migrate

# if [[ $CREATE_SUPERUSER ]];
# then
#   python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
# fi