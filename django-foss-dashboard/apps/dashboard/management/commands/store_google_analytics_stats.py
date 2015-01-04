from django.core.management.base import BaseCommand

from dashboard.measurements import store_google_analytics_stats


class Command(BaseCommand):
    help = 'store google analytics stats'

    def handle(self, *args, **options):
        store_google_analytics_stats()
