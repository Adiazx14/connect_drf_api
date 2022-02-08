from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="adiazx14").exists():
            User.objects.create_superuser("username", "email@gmail.com", "pass")
