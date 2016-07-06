from __future__ import unicode_literals

from django.db import models


class Rssf(models.Model):
    title = models.CharField(max_length=128)
    url = models.URLField()

    def __unicode__(self):
    	return self.title


class Feed(models.Model):
    title = models.CharField(max_length=256)
    created = models.DateField(auto_now=False, auto_now_add=False)
    url = models.URLField()
    author = models.CharField(max_length=256)
    image_url = models.URLField()

    def __unicode__(self):
        return self.title
