#!/bin/bash
python manage.py makemigrations backend
python manage.py migrate
python create_superuser.py
gunicorn evacuation_management_system.wsgi:application --bind 0.0.0.0:$PORT