from config.settings.base import *


ENV = "dev"
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^)zk=x+rfy_w!64xxkr_zq+2@z+(=!ycy8%_uky=m@1b&fu-&n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS.append(
    'debug_toolbar',
)

INTERNAL_IPS = [
    '127.0.0.1',
]
