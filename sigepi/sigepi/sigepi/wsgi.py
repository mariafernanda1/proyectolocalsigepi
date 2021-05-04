"""
WSGI config for sigepi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sigepi.settings')

#path a donde esta el manage.py de nuestro proyecto Django
sys.path.append('/home/mariafz/Proyectos/sigepi/')

#prevenimos UnicodeEncodeError
os.environ.setdefault("LANG", "es_CO.UTF-8")
os.environ.setdefault("LC_ALL", "es_CO.UTF-8")



application = get_wsgi_application()
