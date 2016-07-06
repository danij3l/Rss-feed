from django.core.management.base import BaseCommand, CommandError
from rssf.models import Rssf, Feed
from datetime import datetime


class Command(BaseCommand):
    help = "Saves active feed entries in DB"

    def handle(self, *args, **options):
        for rss in Rssf.objects.all():
            new_feed = Feed.objects.create(title=rss.title,
                created=datetime.now(), url=rss.url)
            new_feed.save()
            self.stdout.write(self.style.SUCCESS(
                'Importing:"%s" feed.' % rss))
