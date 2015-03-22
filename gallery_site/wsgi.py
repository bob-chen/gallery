"""
WSGI config for gallery_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gallery_site.settings")

try:
    from os.path import abspath,dirname,join
    sys.path.insert(0,abspath(join(dirname(__file__),"./")))
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
except Exception, ex:
    print ex

#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()