"""
WSGI config for BetacraftCodeAnalyst project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""
import os
import sys

# Add your project directory to the Python path
sys.path.append('/home/django/BetaAnalaysis')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BetacraftCodeAnalyst.settings')

application = get_wsgi_application()

