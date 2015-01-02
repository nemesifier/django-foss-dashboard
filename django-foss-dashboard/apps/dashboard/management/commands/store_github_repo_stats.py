from django.core.management.base import BaseCommand

from dashboard.measurements import store_github_repo_stats


class Command(BaseCommand):
    help = 'track stars, watchers, forks, contributors, repo size'

    def handle(self, *args, **options):
        store_github_repo_stats()
