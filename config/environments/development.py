from config.components.app import INSTALLED_APPS
from config.components.rest_framework import REST_FRAMEWORK


DEVELOPING_APPS = [
    'django_extensions',
]

INSTALLED_APPS.extend(DEVELOPING_APPS)

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].extend([
    'rest_framework.renderers.BrowsableAPIRenderer',
])
