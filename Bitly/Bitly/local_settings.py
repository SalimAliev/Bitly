from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-z*p4k%(k6-g_uzcq1p7sk#g1j1_01=y+o4cvz4)3gm46^iai@!'

DEBUG = True

ALLOWED_HOSTS = ['localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'app_db',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'db',
        'PORT': '5432'
    }
}

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]