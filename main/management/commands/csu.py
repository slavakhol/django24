from django.core.management import BaseCommand

from main.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='',
            first_name='Simple',
            last_name='User',
            is_staff=False,
            is_superuser=False
        )
        user.set_password('')
        user.save()
