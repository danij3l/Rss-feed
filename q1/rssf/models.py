from __future__ import unicode_literals

from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail


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
    image = ImageField(blank=True)

    def save(self, *args, **kwargs):
        if self.image:
            self.image = get_thumbnail(self.image,
                '100x50', quality=99, format='JPEG')
        super(Feed, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
