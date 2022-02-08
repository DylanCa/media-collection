from django.contrib.auth.models import AbstractUser
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class User(AbstractUser):
    pass

class MediaStatusPerUser(TimeStampedModel):

    STATUS = (("watched", "watched"), ("read", "read"), ("ongoing", "ongoing"))
    resource_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    resource = GenericForeignKey('resource_type', 'resource_id')
    resource_id = models.PositiveIntegerField()
    status = models.CharField(default="ongoing", choices=STATUS, max_length=10)
    user = models.ForeignKey(to=User, related_name="user_episodes", on_delete=models.CASCADE)

    class Meta:
        unique_together = [['user', 'resource_id', 'resource_type']]
