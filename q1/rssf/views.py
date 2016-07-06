from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from .models import Rssf, Feed
from .forms import RssfForm


def rssf_list(request):
    if request.method == "POST":
        form = RssfForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        form = RssfForm()

	queryset = Rssf.objects.all()
	context = {
		"object_list": queryset,
		"title": "List of RSSFeeds:",
		"form":form,
	}

	return render(request, "rssf_list.html", context=context)

def feed_list(request):
    feeds = Feed.objects.all().order_by('-created')
    context = {"feed_list": feeds}

    return render(request, "feed_list.html", context=context)
