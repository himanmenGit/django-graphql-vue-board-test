import os

SETTINGS_MODULE = os.environ.get('DJANGO_SETTINGS_MODULE')
if not SETTINGS_MODULE or SETTINGS_MODULE == 'app.config.settings':
    from .local import *
