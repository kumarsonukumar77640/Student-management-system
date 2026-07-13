from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User.objects.create_superuser(
            username="sonuadmin",
            email="Kumarsonukumar77640@gmail.com",
            password="sonuadmin"
        )
        self.stdout.write("Admin Created")
        