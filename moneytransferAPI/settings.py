from pathlib import Path
import os
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1$smmz0mieyc4-9iwse(pxxfa*jhm0j6#e)#0%1+&e$8gvi(7j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'graphene_django',
    'user_controller',
    'djmoney.contrib.exchange',
    'Transanctions',
    'Wallet'
]



AUTH_USER_MODEL = "user_controller.User"

ALLOWED_HOSTS = ["*"]





MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'moneytransferAPI.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'moneytransferAPI.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DB_NAME = config("DB_NAME")
DB_USER = config("DB_USER")
DB_PASSWORD = config("DB_PASSWORD")
DB_HOST = config("DB_HOST")
DB_PORT = config("DB_PORT")




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD':DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
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



# AWS CONFIG
AWS_STATIC_LOCATION = 'static'
S3_BUCKET_URL       = config('S3_BUCKET_URL')
STATIC_ROOT         = 'staticfiles'

AWS_ACCESS_KEY_ID     =  config('AWS_S3_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY =  config('AWS_S3_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_HOST_REGION         = config('AWS_HOST_REGION')
AWS_S3_CUSTOM_DOMAIN    = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_DEFAULT_ACL         = None

AWS_LOCATION            = 'static'
MEDIA_URL               = 'media/'
AWS_QUERYSTRING_AUTH    = False


STATICFILES_DIRS        = [
    os.path.join(BASE_DIR, 'static'),
        ]
STATIC_URL              = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
DEFAULT_FILE_STORAGE    = 'moneytransferAPI.storage_backends.MediaStorage'
STATICFILES_STORAGE     = 'moneytransferAPI.storage_backends.MediaStorage'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

GRAPHENE = {
    'SCHEMA': 'moneytransferAPI.schema.schema',
    'MIDDLEWARE': [
        'moneytransferAPI.middlewares.CustomAuthMiddleware',
        'moneytransferAPI.middlewares.CustomPaginationMiddleware'
        ],
        'PAGE_SIZE': 5
}

CORS_ALLOW_ALL_ORIGINS = True
