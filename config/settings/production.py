from .base import *
import os

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = False

ALLOWED_HOSTS = [os.getenv('ALLOWED_HOSTS')]



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': os.getenv('DB_NAME'),
       'USER': os.getenv('DB_USER'),
       'PASSWORD': os.getenv('DB_PASSWORD'),
       'HOST': os.getenv('DB_HOST'),
       'PORT': os.getenv('DB_PORT'),
   }
}
