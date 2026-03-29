import os
from django.core.wsgi import get_wsgi_application

# Substitua 'setup_django.settings' pelo caminho correto se sua pasta tiver outro nome
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup_django.settings')

application = get_wsgi_application()
