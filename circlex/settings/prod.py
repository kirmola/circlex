from circlex.settings_base import *
from django.core.management.utils import get_random_secret_key

ALLOWED_HOSTS = []

DEBUG = False

SECRET_KEY = get_random_secret_key()

DATABASES = {}


ROOT_URLCONF = 'circlex.urls'