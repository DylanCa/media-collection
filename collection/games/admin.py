from django.contrib import admin
from .models import Game, Genre, Platform

# Register your models here.
class GameAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "cover_image",
    )


class PlatformAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


admin.site.register(Game, GameAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Genre, GenreAdmin)
