from .base import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fcp40&eqr*=e7k2lmb+2d&)ph00m$=5m9_v1iuxe5-n8126t1g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'bucketlist_dev',
       'USER': 'bucketlist_dev',
       'PASSWORD': 'dev_insecure',
       'HOST': 'localhost',
       'PORT': '5432',
   }
}
