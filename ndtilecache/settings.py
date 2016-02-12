"""
Django settings for open-connectome project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import settings_secret
from ndtilecachepaths import NDTILECACHE_NDLIB_PATH

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = settings_secret.SECRET_KEY

SITE_ID = 1

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tilecache',
    'djcelery',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'ndtilecache.urls'

TEMPLATES = [
]

WSGI_APPLICATION = 'ndtilecache.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ndtilecache_django',
        'USER': settings_secret.USER,
        'PASSWORD': settings_secret.PASSWORD,
        'HOST': settings_secret.HOST,
        'PORT': '',
    
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# URL prefix for static files.
STATIC_URL = '/static/'

# Absolute path to the directory static files should be collected to.
STATIC_ROOT = ''

# Additional locations of static files
STATICFILES_DIRS = (
)

# List of finder classes that know how to find static files in various locations.
STATICFILES_FINDERS = (
  "django.contrib.staticfiles.finders.FileSystemFinder",
  "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)


# Logging config
LOGGING = {
  'version': 1,
  'disable_existing_loggers': True,
  'formatters': {
    'standard': {
      'format': "[%(asctime)s] %(levelname)s [%(name)s:%(module)s:%(lineno)s]%(message)s",
      'datefmt': "%d/%b/%Y %H:%M:%S"
    },
  },
  'handlers': {
    # 'null': {
      # 'level': 'DEBUG',
      # 'class': 'django.utils.log.NullHandler'
    # },
    'logfile': {
      'level': 'DEBUG',
      'class': 'logging.handlers.RotatingFileHandler',
      'filename': '/var/log/ndtilecache/ndtilecache.log',
      'maxBytes': 500000,
      'backupCount' : 7,
      'formatter': 'standard',
    },
    'console': {
      'level': 'INFO',
      'class': 'logging.StreamHandler',
      'formatter': 'standard',
    }
  },
  'loggers': {
    'django': {
      'handlers': ['console'],
      'level': 'DEBUG',
      'propagate': True,
    },
    'django.db.backends': {
      'handlers': ['console'],
      'level': 'DEBUG',
      'propagate': False,
    },
    'ndtilecache': {
      'handlers': ['console', 'logfile'],
      'level': 'WARN',
    }
  },
}

# NDTILECACHE Settings
# SERVER = 'openconnecto.me/ocp'
SERVER = 'localhost:8080'
DBNAME = 'ndtilecache'
TILESIZE = 512
CACHE_DIR = settings_secret.CACHE_DIR
CACHE_SIZE = 1000000 # In MB

# Celery Settings
BROKER_URL = 'amqp://guest@localhost'
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json', 'pickle']
CELERYD_PREFETCH_MULTIPLIER = 1
