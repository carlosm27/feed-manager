from django.shortcuts import render, redirect
import feedparser
from .models import Author
from .form import AuthorForm
from .rss_content.rss_info import Rss_info
# Create your views here.


"""
Display all the articles from a RSS link.
"""
def feed_view(request):
    context = {}
    if request.method == 'GET':
        link = request.GET.get("rss_link", "")
        rss_link = Rss_info(link)
        entries_links = rss_link.list_links()
        print(entries_links)
        context['entries'] = entries_links
    return render(request, "rss_follower/rss_feed.html", context)    



def author_form(request):
    authors = Author.objects.all()
    form = AuthorForm()
    
    if request.method == 'POST':
        form =AuthorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("list-authors")   
    context = {
        'form' : form,
        'authors': authors,
    }  
    return render(request, "rss_follower/author_form.html", context)     

"""
Add a author to the database
"""

def add_link_view(request):
    authors = {}
    if request.method == 'POST':
        feed_link = request.GET.get("rss_link", "")
        author_name = request.GET.get("name", "")
        author = Author(name=author_name, rss_link=feed_link)
        author.save()

        authors = Author.objects.all()
    context = {"authors": authors}
    return render(request, "rss_follower/list_authors.html", context)

"""
List of all authors in the database
"""
def list_authors(request):
    authors = Author.objects.all()
    context = {"authors": authors}
    return render(request, "rss_follower/list_authors.html", context)


    
