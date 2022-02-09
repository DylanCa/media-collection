from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MediaStatusPerUser, User

# Register your models here.
admin.site.register(User, UserAdmin)


class MediaStatusAdmin(admin.ModelAdmin):
    list_display = ("id", "resource", "status", "user", )

admin.site.register(MediaStatusPerUser, MediaStatusAdmin)
