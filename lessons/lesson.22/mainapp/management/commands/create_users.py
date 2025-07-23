from django.core.management.base import BaseCommand, CommandError
from userapp.models import MyUser
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = "Fill db with test data"

    def handle(self, *args, **options):
        try:
            MyUser.objects.create_user('user', 'user@user.com', 'user')
        except IntegrityError:
            self.stdout.write(
                self.style.SUCCESS('Already Exists')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS('Done')
            )

        try:
            MyUser.objects.create_user('foodmaster', 'foodmaster@foodmaster.com', 'foodmaster')
        except IntegrityError:
            self.stdout.write(
                self.style.SUCCESS('Already Exists')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS('Done')
            )
