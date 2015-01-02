from django.core.management.base import BaseCommand

from dashboard.measurements import store_mailman2_list_subscribers


class Command(BaseCommand):
    help = 'track mailing list subscribers'

    def handle(self, *args, **options):
        store_mailman2_list_subscribers()
