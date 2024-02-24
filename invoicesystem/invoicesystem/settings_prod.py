from .settings import *

BASE_DIR = Path(__file__).resolve().parent.parent
ALLOWED_HOSTS = ['*','localhost','127.0.0.1']

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "djangowebsite",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "postdb",
        "PORT": "5432",
    }
}

DEBUG = False
#Security Settings
#Redirect to https for http requests
# SECURITY WARNING: don't run with debug turned on in production!
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SSL_REDIRECT = True