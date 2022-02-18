from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = 'w%j5d5=mn8_8wj2@r8va5^w7#=uay_o7_e=1q-8_8wcyd4-%m+'

# django_debug_tool
INTERNAL_IPS = [
    '127.0.0.1',
]

BASE_BACKEND_URL = 'http://localhost:8000'
BASE_FRONTEND_URL = 'http://localhost:3000'

# CORS SETTINGS
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
