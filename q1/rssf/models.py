from __future__ import unicode_literals

from django.db import models

class Rssf(models.Model):
    title = models.CharField(max_length=128)
    url = models.CharField(max_length=256)

    def __unicode__(self):
    	return self.title
