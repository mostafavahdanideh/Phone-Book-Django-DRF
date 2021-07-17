"""
Django settings for mywebapp_project project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)3dyqd&9)!8!$_@fn2_ki!2k%hzv*y+157jfg&@e5$kq*$#@%!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'rest_framework',
    "django_static_fontawesome",
    "info.apps.InfoConfig",
    "home.apps.HomeConfig",
    'users.apps.UsersConfig',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
INTERNAL_IPS = [
    '127.0.0.1',
]

ROOT_URLCONF = 'phonebook_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'info.context_processor.user_phone_finder',
            ],
        },
    },
]

WSGI_APPLICATION = 'phonebook_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "phonebook",
        'USER': 'mostafa_vm',
        'PASSWORD': '12345678910',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console_handler': {
            'class': 'logging.StreamHandler',
        },
        'users_handler': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'system_logs', 'users.log'),
            'formatter': 'simple',
            'filters': ['require_debug_true']
        },
        'info_handler': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'system_logs', 'phone_book.log'),
            'formatter': 'verbose',
            'filters': ['require_debug_true']
        },
        'home_handler': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'system_logs', 'home.log'),
            'formatter': 'simple',
            'filters': ['require_debug_true']
        },
        'users_signals_handler': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'system_logs', 'users_signals.log')
        }
    },
    # this is root logger
    'root': {
        'handlers': ['console_handler', ],
        'level': 'ERROR',
        'propagate': False,
    },
    'loggers': {
        'info.views': {
            'handlers': ['info_handler', ],
            'level': 'INFO',
            'propagate': False,
        },
        'users.signals': {
            'handlers': ['users_signals_handler', ],
            'level': 'DEBUG',
            'propagate': False,
        },
        'users': {
            'handlers': ['users_handler', ],
            'level': 'DEBUG',
            'propagate': False,
        },
        'home': {
            'handlers': ['home_handler', ],
            'level': 'WARNING',
            'propagate': False,
        }
    },
}

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"


# LANGUAGES = [
#     ('fa', ('Persian')),
#     ('en', ('English')),
# ]


LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]
LANGUAGE_CODE = 'fa' # destination language

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = "user:login"
LOGIN_REDIRECT_URL = "home:home"
LOGOUT_REDIRECT_URL = "home:home"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = ""
STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SESSION_EXPIRE_SECONDS = 60 * 10  # 600seconds = 10 minutes
