from django.contrib.contenttypes.models import ContentType
from rest_framework_json_api import serializers

from collection.users.models import User, MediaStatusPerUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
        )
        read_only_fields = (
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
        )


class MediaStatusPerUserSerializer(serializers.ModelSerializer):
    resource_type = serializers.CharField(required=True)

    class Meta:
        model = MediaStatusPerUser
        fields = (
            "resource_type",
            "resource_id",
            "status",
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
