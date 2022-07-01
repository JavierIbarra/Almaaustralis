from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


CORS_ALLOWED_ORIGINS = [
    'http://almaaustralis.cl/',
    'http://www.almaaustralis.cl/',
    'https://almaaustralis.cl/',
    'https://www.almaaustralis.cl/',
]