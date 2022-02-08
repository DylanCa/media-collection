from django.db import models

class Show(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    cover = models.URLField(null=True, blank=True)

    def get_seasons_count(self):
        pass

    def get_episodes_count(self):
        pass


class Season(models.Model):
    show = models.ForeignKey(to=Show, related_name="seasons" ,on_delete=models.CASCADE)
    season_number = models.IntegerField(null=False, blank=False)


class Episode(models.Model):
    season = models.ForeignKey(to=Season, related_name="episodes" ,on_delete=models.CASCADE)
    episode_number = models.IntegerField(null=False, blank=False)
    name = models.CharField(max_length=128, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
