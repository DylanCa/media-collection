from django.db import models


class Collection(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False, unique=True)
    cover_image = models.URLField(null=True, blank=True)

class Movie(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False, unique=True)
    description = models.TextField(null=True, blank=True)
    cover_image = models.URLField(null=True, blank=True)
    collection = models.ForeignKey(to=Collection, related_name="movies", null=True, blank=True, on_delete=models.SET_NULL)