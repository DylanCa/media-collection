from django.contrib import admin
from .models import Show, Season, Episode

# Register your models here.
class ShowAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")


class SeasonAdmin(admin.ModelAdmin):
    list_display = ("id", "show", "season_number")


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ("id", "season", "episode_number", "name")


admin.site.register(Show, ShowAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Episode, EpisodeAdmin)
