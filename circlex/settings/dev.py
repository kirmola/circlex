from circlex.settings_base import *
from os import environ
from dotenv import load_dotenv
load_dotenv()



ALLOWED_HOSTS = ["*"]

DEBUG = True


SECRET_KEY = environ["SECRET_KEY"]

INSTALLED_APPS += [
    'django_browser_reload',
    "debug_toolbar",

]


MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",

]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


ROOT_URLCONF = 'circlex.urls_dev'

NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

INTERNAL_IPS = [
    "127.0.0.1"
]