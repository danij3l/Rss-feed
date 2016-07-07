from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic import DetailView, TemplateView
from .models import Rssf, Feed
from .forms import RssfForm
import re


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

class FeedDetailView(DetailView):
    template_name = "feed.html"
    model = Feed


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of
    unecessary spaces and grouping quoted words together.
        Example:

        >>> normalize_query('  some random  words "with   quotes  " and
        spaces') ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    '''
    return [normspace(' ',
        (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects.
        That combination aims to search keywords within a model
        by testing the given search fields.
    '''
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        entry_query = get_query(query_string, ['title'])

        found_entries = Feed.objects.filter(entry_query).order_by('-created')

    return render_to_response("search_by_author.html",
                          { 'query_string': query_string,
                          'found_entries': found_entries },
                        context_instance=RequestContext(request))
