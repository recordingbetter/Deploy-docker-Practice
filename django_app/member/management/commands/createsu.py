import json

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        config_secret_common = json.loads(open(settings.CONFIG_SECRET_COMMON_FILE).read())
        username = config_secret_common['django']['default_superuser']['username']
        password = config_secret_common['django']['default_superuser']['password']
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                    username=username,
                    password=password,
                    email='',
            )
            print('Superuser {} created!'.format(username))
        else:
            print('Superuser {} is already exists!'.format(username))
