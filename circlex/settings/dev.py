from circlex.settings_base import *
from os import environ
from dotenv import load_dotenv
load_dotenv()



ALLOWED_HOSTS = ["*"]

DEBUG = True


SECRET_KEY = environ["SECRET_KEY"]

INSTALLED_APPS += [

]

MIDDLEWARE += [

]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


ROOT_URLCONF = 'circlex.urls_dev'
