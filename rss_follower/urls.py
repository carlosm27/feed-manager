from django.urls import path
from . import views

urlpatterns = [
    path("rss_feed", views.feed_view, name="rss_feed"),
]