# *-* coding:utf-8
# Django settings for django_news project.
import os
PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
RESOURCE_PATH     = os.path.join(PROJECT_ROOT_PATH,'resource')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Pedro Victor', 'pedro_jampa86@yahoo.com.br'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'django_news',                # Or path to database file if using sqlite3.
        'USER': 'root',                       # Not used with sqlite3.
        'PASSWORD': '1234',                   # Not used with sqlite3.
        'HOST': '',                           # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                           # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Sao_Paulo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pt-br'

LANGUAGES = (
    ('pt-br', u'Português'),
    ('en', u'Inglês'),
    ('es', u'Espanhol'),
)

LOCALE_PATHS = (
    os.path.join(RESOURCE_PATH,'locale'),
)

#SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(RESOURCE_PATH,'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(RESOURCE_PATH,'root')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(RESOURCE_PATH,'static'),
)

CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT,'ckeditor')

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '8c@t-eeysa0ee(p#@)0#jfbh*y^=d+c7o0&amp;q3x)rw#b%!!5!b+'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
     #procura os templates a partir do TEMPLATE_DIRS
    'django.template.loaders.filesystem.Loader',
     # procura os templates a partir da pasta "template"
     # em cada aplicação registrada
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',

    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_news.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'django_news.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates".
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT_PATH,'templates'),
)

#registra todas as aplicações
#utilizadas pelo django
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.syndication',
    'django.contrib.flatpages',
    'django.contrib.comments',
    'django.contrib.sitemaps',
    'django.contrib.redirects',
    'noticias',
    'blog',
    'ckeditor',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
# Type of cache in use
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

#The number of seconds each page should be cached.
CACHE_MIDDLEWARE_SECONDS= 1
CACHE_MIDDLEWARE_KEY_PREFIX= 'django_news'
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

try:
    from local_settings import *
except:
    pass
