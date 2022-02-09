from django.contrib.contenttypes.models import ContentType
from rest_framework_json_api import serializers
from generic_relations.relations import GenericRelatedField

from collection.movies.api.serializers import CollectionSerializer, MovieSerializer
from collection.shows.api.serializers import (
    EpisodeSerializer,
    SeasonSerializer,
    ShowSerializer,
)

from collection.shows.models import (
    Episode,
    Season,
    Show,
)

from collection.movies.models import (
    Movie,
    Collection,
)

from collection.users.models import User, MediaStatusPerUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
        )


class MediaStatusPerUserSerializer(serializers.ModelSerializer):
    resource_type = serializers.CharField(required=True)
    resource = GenericRelatedField(
        {
            Episode: EpisodeSerializer(),
            Season: SeasonSerializer(),
            Show: ShowSerializer(),
            Movie: MovieSerializer(),
            Collection: CollectionSerializer(),
        },
        read_only=True,
    )

    class Meta:
        model = MediaStatusPerUser
        fields = (
            "status",
            "has_liked",
            "resource_type",
            "resource",
            "resource_id",
        )

    def validate_resource_type(self, value):
        try:
            return ContentType.objects.get(model=value)
        except ContentType.DoesNotExist:
            raise serializers.ValidationError({"contentType": "Can't be found"})

    def validate(self, attrs):
        if (not self.instance) and ("user_id" not in attrs):
            if self.context.get("view"):
                attrs["user_id"] = self.context.get("view").kwargs.get("user_pk")
        if "resource_type" in attrs:
            resource = attrs["resource_type"].model_class()
            resource_id = attrs["resource_id"]
            if not resource.objects.get(id=resource_id):
                raise resource.DoesNotExist

        return attrs
