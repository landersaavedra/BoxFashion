BEFORE_DJANGO_APPS = (

)

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',

    # Esta esa nueva para django-allauth
    'django.contrib.sites',

    'django.contrib.humanize',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    'WebBoxFashion.apps.flow',
    'WebBoxFashion.apps.website',
    'WebBoxFashion.apps.security',
  
)

THIRD_PARTY_APPS = (
    'solo',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
)


INSTALLED_APPS = BEFORE_DJANGO_APPS + DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

SITE_ID = 1