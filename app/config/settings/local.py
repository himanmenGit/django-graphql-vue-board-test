from .base import *

DEBUG = True
ALLOWED_HOSTS = []
WSGI_APPLICATION = 'app.config.wsgi.local.application'
INSTALLED_APPS += [
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
