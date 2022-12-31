from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=20)
    rss_link = models.URLField(max_length=200)
    num_entries = models.IntegerField()
    last_entry = models.CharField(max_length=200)