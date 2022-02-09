from django.db import models

class Platform(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False, unique=True)

class Genre(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False, unique=True)

class Game(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False, unique=True)
    description = models.TextField(null=True, blank=True)
    platforms = models.ManyToManyField(to=Platform, related_name="games", blank=True)
    genres = models.ManyToManyField(to=Genre, related_name="games", blank=True)
    cover_image = models.URLField(null=True, blank=True)