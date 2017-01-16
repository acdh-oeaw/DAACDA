from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vyo+k2s_!aaa=$2w_w8=qlzfz8o+#5&lymr+988(i!sd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
