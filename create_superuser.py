# create_superuser.py

import os
from django.contrib.auth import get_user_model
from django.core.wsgi import get_wsgi_application
from decouple import config


os.environ['DJANGO_SETTINGS_MODULE'] = 'evacuation_management_system.settings'
application = get_wsgi_application()

User = get_user_model()

if config('CREATE_SUPERUSER', cast=bool):
    if not User.objects.filter(username=config('DJANGO_SUPERUSER_USERNAME')).exists():
        User.objects.create_superuser(
            username=config('DJANGO_SUPERUSER_USERNAME'),
            email=config('DJANGO_SUPERUSER_EMAIL'),
            password=config('DJANGO_SUPERUSER_PASSWORD'),
        )
    else:
        print("Superuser already exists. Not created.")
