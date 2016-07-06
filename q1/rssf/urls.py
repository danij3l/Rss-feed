from django.conf.urls import url
from django.contrib import admin

from .views import rssf_list, feed_list

urlpatterns = [
	url(r'^$', rssf_list, name='rssf_list'),
    url(r'feeds/$', feed_list, name='feed_list'),
]
