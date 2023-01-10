from django.contrib import admin
from rss_follower.models import Author

class AuthorAdmin(admin.ModelAdmin):
    admin.site.register(Author)

# Register your models here.
