from . import settings

BASE_DIR = settings.BASE_DIR


SECRET_KEY = settings.SECRET_KEY

DEBUG = False

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


INSTALLED_APPS = settings.INSTALLED_APPS

AUTH_USER_MODEL = settings.AUTH_USER_MODEL


MIDDLEWARE = settings.MIDDLEWARE
ROOT_URLCONF = settings.ROOT_URLCONF

TEMPLATES = settings.TEMPLATES
TEMPLATES[0]['DIRS'] = ['/home/stuxnet385/art_gallery/templates']

WSGI_APPLICATION = settings.WSGI_APPLICATION


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stuxnet385$art_gallery',
        'USER': 'stuxnet385',
        'PASSWORD': 'adityakumar',
        'HOST': 'stuxnet385.mysql.pythonanywhere-services.com',
    }
}


AUTH_PASSWORD_VALIDATORS = settings.AUTH_PASSWORD_VALIDATORS


LANGUAGE_CODE = settings.LANGUAGE_CODE

TIME_ZONE = settings.TIME_ZONE

USE_I18N = settings.USE_I18N

USE_L10N = settings.USE_L10N

USE_TZ = settings.USE_TZ


STATIC_URL = settings.STATIC_URL
STATIC_ROOT = settings.STATIC_ROOT
