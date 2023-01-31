from django.urls import path
from . import views
from .views import AuthorDetailView, AuthorListView

urlpatterns = [
    path("rss-feed", views.feed_view, name="rss-feed"),
    path("authors", views.author_form, name='author-form'),
    path("list-authors", views.list_authors, name='list-authors'),
    path("author/<int:pk>", AuthorDetailView.as_view(), name = 'author-detail'),
    path("all-authors", AuthorListView.as_view(), name = "all-authors")
]