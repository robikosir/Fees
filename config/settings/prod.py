from config.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True
ENV = "prod"

STATIC_URL = "/static/"
STATIC_ROOT = "/static_files/"

SECRET_KEY = 'ghashaszh12h589hsnaobn9012u589poabsngka'

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", "34.141.81.19", "35.246.251.238", "34.242.225.178"]

INSTALLED_APPS.append(
    'debug_toolbar',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'ldoLbeXcWNvYgwaeZsOuNFTaKLFCRLsP',
        'PASSWORD': 'GGvT1sOMB9kCyu0BRik1cmZ3qSFPdEuDodMeV3k6u7ek58kb0MmGerYQh46mXJJU',
        'HOST': 'postgres',
        'PORT': 5432,
    }
}
