"""
WSGI config for lockzog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

# add project module to system path
path = os.path.dirname(os.path.abspath(__file__)) + "/.."
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lockzog.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
