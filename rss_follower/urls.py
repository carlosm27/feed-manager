from django.urls import path
from . import views

urlpatterns = [
    path("rss_feed", views.feed_view, name="rss_feed"),
    path("authors", views.author_form, name='author-form'),
    path("list-authors", views.list_authors, name='list-authors'),
    
]