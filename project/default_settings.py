# Django settings for beamerapp project.
import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)
TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)
    
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS


TIME_ZONE = 'Europe/Amsterdam'

LANGUAGE_CODE = 'nl'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = STATIC_URL + 'media/'

SECRET_KEY = '_$&pr_o0%8n$b=y!c*7-=v^_9nv+5(kef!vjt15bd3l7a60=!+'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    # default template context processors
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',

    # required by grappelli and social registration:
    # 'django.core.context_processors.request',

)

ROOT_URLCONF = 'urls'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.webdesign',
    'django.contrib.staticfiles',
    # Project
    # 3rd party
)

INSTALLED_APPS += (
    # Debug:
    'debug_toolbar',
    'django_extensions',
    'django.contrib.admindocs',
)

# For Debug toolbar:
INTERNAL_IPS = ('127.0.0.1')

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

LOGIN_URL = "/user/login/"
LOGIN_REDIRECT_URL = "/"
