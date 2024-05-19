import os
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'evacuation_management_system.settings'
application = get_wsgi_application()

if os.environ.get('CREATE_SUPERUSER'):
    call_command('createsuperuser',
                 username=os.environ.get('DJANGO_SUPERUSER_USERNAME'),
                 email=os.environ.get('DJANGO_SUPERUSER_EMAIL'),
                 interactive=False)
