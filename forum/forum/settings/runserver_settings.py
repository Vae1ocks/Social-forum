import os
from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'forum',
        'USER': 'admin',
        'PASSWORD': 'admin',
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache", # для использования
        "LOCATION": "redis://127.0.0.1:6379",
    }
}

'''
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache', # для тестов
    }
}
'''

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0