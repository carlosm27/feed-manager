from django.urls import path
from . import views
from .views import AuthorDetailView, AuthorListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("rss-feed", views.feed_view, name="rss-feed"),
    path("authors", views.author_form, name='author-form'),
    path("list-authors", views.list_authors, name='list-authors'),
    path("author/<int:pk>", AuthorDetailView.as_view(), name = 'author-detail'),
    path("all-authors", AuthorListView.as_view(), name = "all-authors")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)