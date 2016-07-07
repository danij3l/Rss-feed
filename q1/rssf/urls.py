from django.conf.urls import url
from django.contrib import admin

from .views import rssf_list, FeedsListView, FeedDetailView

urlpatterns = [
	url(r'^$', rssf_list, name='rssf_list'),
    url(r'feeds/$', FeedsListView.as_view(), name='feeds'),
    url(r'feed/(?P<pk>\d+)/$', FeedDetailView.as_view(), name='feed'),
]
