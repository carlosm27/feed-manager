from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    rss_link = models.URLField(max_length=200)
