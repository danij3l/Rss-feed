from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from .models import Rssf, Feed
from .forms import RssfForm
from django.views.generic.list import ListView
from django.views.generic import DetailView


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


class FeedsListView(ListView):
    template_name = "feed_list.html"
    model = Feed
    paginate_by = 20

    def get_queryset(self):
        return self.model.objects.all().order_by("-created")
