"""
Django settings for django_rest_framework_tutorial project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'AAAAB3NzaC1yc2EAAAADAQABAAABgQC7HOCAgactXQC/14/LT2H96Dn45cX0YA8ga+EpBeHo7Yb/AV37B06isKp9zOR6Gi+2SxNtS6zMrYPMpyV5Lp3KYTZPPPn7sCdBx+m97aaMpq62BT+jOObevNBTdDq7cFXvIbn5rYUw2zLVj7D24UnTxivBu+506nVwJ70bJ0r9XzFKtENdKpv1Vcz7N/93fpFqvqQf4xkWpJ5HwAZFHnZAba2x5pOFTRte6eFPKRsIPwCDa3+3HodViMCOYQVBoMyj7Y8u6YZ//Ooq9y4IzyvZm6EZ0VtcNqkbbBCUTnS1/tK3gmIgYWCG50oQex5AaahPoTSoplczhsDJJRsOyYwRdTRUttMfWUfjCm9Dg5Ol615GTEowfAKQfAhByCwNti3YpSW78WFAi5mKPKndePefF7cX1Aa9dWEZFsRutVIYkjjLgpwjxIWG5lSD4k6gZCtWpgLru+vAhaUrAkg5CPryApkypqp1etk2tuTJkYvgWcIvHizCNwNELDFdKZj9THM= 2499059z@student.gla.ac.uk'




# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.AcceptHeaderVersioning',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5
}
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    # 'rest_framework.authtoken',
    'corsheaders',
    'covid',
    'users',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'covid_information_system_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'covid_information_system_backend.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_URL = '/static/'

#CORS
CORS_ALLOW_WHITELIST = {
    'http://127.0.0.1:8080',
    'http://localhost:8080',
}

ALLOWED_HOSTS = ['*']
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = ('*')




AUTH_USER_MODEL='users.User'

