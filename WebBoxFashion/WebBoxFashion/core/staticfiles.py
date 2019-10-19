import os

__STATIC_PATH = os.path.dirname(os.path.dirname(__file__))


STATIC_URL = '/static/'
#MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(__STATIC_PATH, "../WebBoxFashion/static"),
    #os.path.join(__STATIC_PATH, "../WebBoxFashion/media"),
   
)
STATIC_ROOT = os.path.join(__STATIC_PATH, '/static')
#MEDIA_ROOT = os.path.join(__STATIC_PATH, '/media')

