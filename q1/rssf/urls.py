from django.conf.urls import url
from django.contrib import admin

from .views import rssf_list

urlpatterns = [
	url(r'^$', rssf_list, name='list'),
]
