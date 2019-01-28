from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(34m7d(8c+xqe9pv0m%*6dp-@lfm=p(cs&pygsw(_3+*!04kuy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.81.4']


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_testdb',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'USER': 'blog_tester',
        'PASSWORD': 'blog_tester',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
