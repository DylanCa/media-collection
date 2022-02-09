from django.db import models


class Show(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False, unique=True)
    description = models.TextField(null=True, blank=True)
    cover_image = models.URLField(null=True, blank=True)


class Season(models.Model):
    show = models.ForeignKey(to=Show, related_name="seasons", on_delete=models.CASCADE)
    season_number = models.IntegerField(null=False, blank=False)
    name = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    cover_image = models.URLField(null=True, blank=True)

    class Meta:
        unique_together = [["show", "season_number"]]


class Episode(models.Model):
    season = models.ForeignKey(
        to=Season, related_name="episodes", on_delete=models.CASCADE
    )
    episode_number = models.IntegerField(null=False, blank=False)
    name = models.CharField(max_length=128, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    cover_image = models.URLField(null=True, blank=True)

    class Meta:
        unique_together = [["season", "episode_number"]]