from django.core.management.base import BaseCommand
from django.utils import timezone

class Command(BaseCommand):
    help = 's3 path upload env'

    def handle(self, *args, **kwargs):
        print('hello')
