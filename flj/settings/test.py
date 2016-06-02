from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vyo+k2s_!aaa=$2w_w8=qlzfz8o+#5&lymr+988(i!sd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'autocomplete_light',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'rest_framework',
    'webpage',
    'places',
    'labels',
    'crew',
    'bomber',
    'django_extensions',
    'django_tables2'
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticatedOrReadOnly',),
    'PAGE_SIZE': 10
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
