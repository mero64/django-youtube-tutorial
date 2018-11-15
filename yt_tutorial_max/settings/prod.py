from yt_tutorial_max.settings.base import *

# Override base.py settings here
DEBUG = False

# Insecure! Change later
ALLOWED_HOSTS = ['*']

# Add prod database here later
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


try:
    from yt_tutorial_max.settings.local import *
except:
    pass
