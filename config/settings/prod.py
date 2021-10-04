from config.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
from fees.common.sms.vonage_sms_manager import VonageSmsManager

DEBUG = True
ENV = "prod"

STATIC_URL = "/static/"
STATIC_ROOT = "/static_files/"

SECRET_KEY = 'ghashaszh12h589hsnaobn9012u589poabsngka'

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", "34.141.81.19", "35.246.251.238"]

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

vonage_api_key = "7b26c38b"
vonage_api_secret = "oIugTHFhR1aOgImM"
SMS_MANAGER = VonageSmsManager('Promoklik SMS', vonage_api_key, vonage_api_secret)
