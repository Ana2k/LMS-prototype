"""
WSGI config for loan_management_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loan_management_system.settings')
settings_module = 'loan_management_system.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'loan_management_system.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()

#HERE CAN BE SOME NAMING ISSUES OR ANY ERRORS THAT ARISE.
