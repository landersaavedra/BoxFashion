import os

__PATH_MEDIA = os.path.dirname(os.path.dirname(__file__))

MEDIA_URL = '/media/'


STATICFILES_DIRS = (
    os.path.join(__PATH_MEDIA, "../WebBoxFashion/media"),
    os.path.join(__PATH_MEDIA, "../WebBoxFashion/apps/security/media"),
)

MEDIA_ROOT = os.path.join(__PATH_MEDIA, '../media/')