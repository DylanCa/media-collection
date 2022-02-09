import json
from rest_framework import viewsets, status, mixins
from rest_framework_nested.viewsets import NestedViewSetMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema


from collection.users.api.serializers import (
    UserSerializer,
    MediaStatusPerUserSerializer,
)
from collection.users.permissions import IsOwner
from collection.utils.filters import FilterViewSetMixin
from ..models import MediaStatusPerUser, User


class MeViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    resource_name = "me"

    def list(self, request, *args, **kwargs):
        user = self.request.user
        serializer = self.get_serializer(user)

        return Response(serializer.data)

    @action(methods=["GET"], detail=False)
    def mediastatus(self, request, *args, **kwargs):
        self.resource_name = "mediastatus"
        user = self.request.user
        queryset = MediaStatusPerUser.objects.filter(user=user)
        serializer = MediaStatusPerUserSerializer(queryset, many=True)

        return Response(serializer.data)


class UserViewSet(FilterViewSetMixin, viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    resource_name = "users"


class MediaStatusViewSet(FilterViewSetMixin, NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = MediaStatusPerUserSerializer
    queryset = MediaStatusPerUser.objects.all()
    resource_name = "mediastatus"
    parent_lookup_kwargs = {"user_pk": "user_id"}

    def get_parent_object(self):
        return User.objects.get(id=self.kwargs["user_pk"])

    def get_object(self):
        return MediaStatusPerUser.objects.get(id=self.kwargs["pk"])

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            permission_classes = (IsOwner,)
        else:
            permission_classes = (IsAuthenticated,)

        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        user = self.get_parent_object()
        queryset = self.filter_queryset(self.queryset).filter(user_id=user.id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        mediastatus = self.get_object()
        serializer = self.get_serializer(mediastatus)
        return Response(serializer.data)
