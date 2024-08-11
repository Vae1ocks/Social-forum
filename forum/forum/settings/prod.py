import os
from .base import *


DEBUG = False

ALLOWED_HOSTS = ['62.217.180.165']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://redis:6379",
    }
}


REDIS_HOST = 'redis'
REDIS_PORT = 6379
REDIS_DB = 0

CELERY_BROKER_URL = 'amqp://guest:guest@rabbitmq:5672'
CELERY_RESULT_BACKEND = 'redis://redis3:6379/0'