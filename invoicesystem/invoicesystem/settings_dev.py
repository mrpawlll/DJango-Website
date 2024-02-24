from .settings import *

BASE_DIR = Path(__file__).resolve().parent.parent
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "djangowebsite",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
DEBUG = True