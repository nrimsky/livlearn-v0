from pathlib import Path
import os

import django_heroku

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

DEBUG = False

if DEBUG:
    SECRET_KEY = 'pjx@&_p=!sxc1+c)^8y6%oka2au=acj2a&0bhp6h%rzto_t-cq'
    EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
    EMAIL_FILE_PATH = str(BASE_DIR.joinpath('sent_emails'))
else:
    SECRET_KEY = os.getenv("SECRET_KEY")
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp-relay.sendinblue.com'
    EMAIL_PORT = '587'
    EMAIL_HOST_USER = 'nina@toilets4london.com'
    EMAIL_HOST_PASSWORD = os.getenv("EMAIL_PASSWORD")
    EMAIL_USE_TLS = True
    EMAIL_USE_SSL = False
    DEFAULT_FROM_EMAIL = 'donotreply@howshouldilearn.com'
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True

ALLOWED_HOSTS = ["0.0.0.0", "localhost", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'import_export',
    'links',
    'authapp',
    'bootstrap4'
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'howdoilearnthat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

WSGI_APPLICATION = 'howdoilearnthat.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR, ]


AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
]

if DEBUG:
    from dotenv import load_dotenv
    load_dotenv()

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'email',
        ],
        'APP': {
            'client_id': os.getenv("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY"),
            'secret': os.getenv("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET"),
            'key': ''
        }
    },
    'facebook': {
        'SCOPE': [
            'email',
        ],
        'APP': {
            'client_id': os.getenv("SOCIAL_AUTH_FACEBOOK_KEY"),
            'secret': os.getenv("SOCIAL_AUTH_FACEBOOK_SECRET"),
            'key': ''
        },
        "AUTH_PARAMS": {
            "access_type": "online",
        }
    },
}

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_SUBJECT_PREFIX = "How Should I Learn "
LOGIN_REDIRECT_URL = 'links:index'
LOGIN_URL = 'account_login'
LOGOUT_URL = 'account_logout'
ACCOUNT_SESSION_REMEMBER = True
# ACCOUNT_SIGNUP_FORM_CLASS = "authapp.forms.CustomSignupForm"
SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_EMAIL_VERIFICATION = False
SOCIALACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_QUERY_EMAIL = True


if not DEBUG:
    django_heroku.settings(locals())

