import os
from django.contrib.auth import get_user_model
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'evacuation_management_system.settings'
application = get_wsgi_application()

User = get_user_model()

if os.environ.get('CREATE_SUPERUSER'):
    if not User.objects.filter(username=os.environ.get('DJANGO_SUPERUSER_USERNAME')).exists():
        User.objects.create_superuser(
            username=os.environ.get('DJANGO_SUPERUSER_USERNAME'),
            email=os.environ.get('DJANGO_SUPERUSER_EMAIL'),
            password=os.environ.get('DJANGO_SUPERUSER_PASSWORD'),
        )
    else:
        print("Superuser already exists. Not created.")
