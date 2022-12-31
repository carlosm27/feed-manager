from django.shortcuts import render
import feedparser
# Create your views here.

def feed_view(request):
    context = {}
    if request.method == 'GET':
        link = request.GET.get("rss_link", "")
        entries_links = list_links(link)
        context['entries'] = entries_links
    return render(request, "rss_follower/rss_feed.html", context)    






def list_links(link: str):
    feed = feedparser.parse(link)

    lst = []
    for entry in feed['entries']:
        lst.append(entry.links[0]['href'])
    return lst
