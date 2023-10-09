from django.core.management.base import BaseCommand
from mystore.models import User


class Command(BaseCommand):
    help = "Print 'Hello world!' to output."

    def handle(self, *args, **kwargs):
        user = User(firstname='John', email='john@example.com', phone_number='+79509500304')
        user.save()
