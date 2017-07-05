from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

# WSGI application
WSGI_APPLICATION = 'config.wsgi.deploy.application'

# Static URLs
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static_root')


DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = config_secret_deploy['django']['database']

# print('@@@@@@@ DEBUG:', DEBUG)
# print('@@@@@@@ ALLOWED_HOSTS:', ALLOWED_HOSTS)