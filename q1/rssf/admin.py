from django.contrib import admin
from .models import Rssf, Feed


class FeedModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Feed

    list_display = ["id", "created", "title", "url", "author"]
    list_display_links = ["id"]
    list_editable = ["title", "url", "author"]
    list_filter = ["created", "author"]

    search_fields = ["title", "content"]


admin.site.register(Rssf)
admin.site.register(Feed, FeedModelAdmin)
