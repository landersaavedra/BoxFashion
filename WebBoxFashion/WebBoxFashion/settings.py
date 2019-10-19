import os
from .core.internationalization import *
from .core.applist import *
from .core.json_settings import get_settings
from .core.staticfiles import *
from .core.mediafiles import *
from .core.mailserver import *

settings = get_settings()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = settings['SECRET_KEY']
DEBUG = settings['DEBUG']
ALLOWED_HOSTS = settings['SECURITY']['ALLOWED_HOSTS']
DATABASES = settings['DB']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'WebBoxFashion.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'WebBoxFashion/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries':{
            'add_class':'WebBoxFashion.apps.flow.templatetags.add_class',}
        },
    },
]

WSGI_APPLICATION = 'WebBoxFashion.wsgi.application'
AUTH_PASSWORD_VALIDATORS = settings['AUTH_PASSWORD_VALIDATORS']
LOGIN_URL = '/security/login/'