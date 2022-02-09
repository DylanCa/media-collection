from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Movie, Collection

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "collection", )

class CollectionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "cover_image", )

admin.site.register(Movie, MovieAdmin)
admin.site.register(Collection, CollectionAdmin)
