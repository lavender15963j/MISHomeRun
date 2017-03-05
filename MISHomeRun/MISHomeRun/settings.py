#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Django settings for MISHomeRun project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-8=w9hhf5s+k^dy@8crul*g%ko+#wd7o-2-w7)n477dyr#0a=j'

# SECURITY WARNING: don't run with debug turned on in production!
from Iuno import DEVELOPMENT, STAGE, PRODUCTION

SERVER_MODE = (DEVELOPMENT if 'SERVER_MODE' not in os.environ else
               locals()[(os.environ['SERVER_MODE'])])

DEBUG = True if SERVER_MODE not in (STAGE, PRODUCTION) else False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 

    'main',
    'customer',
    'game',
    'team',
    'betting',
    'forum',

    'Iuno.member',

    'django_extensions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'MISHomeRun.urls'

AUTH_USER_MODEL = 'main.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                os.path.join(BASE_DIR, 'templates'),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MISHomeRun.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)
    
if DEBUG:
    STATIC_ROOT = location('static')
    
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

#=========================================================================
# Iuno 
#=========================================================================
APP_NAME = 'MISHomeRun'
APP_VERSION = "1.0.0.0" # "$Revision: 133 $"[11:-2]

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.mishomerun.com']

USE_X_FORWARDED_HOST = True

IUNO_MEMBER_ENABLE = True

import Iuno
Iuno.attachSettings(locals())

# Iuno.member


# Always use localhost static, not static.nuwainfo.com.
STATIC_URL = '/static/' 