from rest_framework import viewsets, status, response, mixins
from rest_framework_nested.viewsets import NestedViewSetMixin

from collection.shows.api.serializers import (
    EpisodeSerializer,
    SeasonSerializer,
    ShowSerializer,
)
from ..models import Show, Season, Episode


class ShowViewSet(viewsets.ModelViewSet):
    serializer_class = ShowSerializer
    queryset = Show.objects.all()
    resource_name = "shows"
    permission_classes = ()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        show = serializer.create(serializer.validated_data)

        for season in request.data["seasons"]:
            new_season = Season()
            new_season.show = show
            new_season.season_number = season["season_number"]
            new_season.name = season["name"]
            new_season.description = season["overview"]
            new_season.cover = season["poster_path"]
            new_season.save()

        queryset = Show.objects.get(name=show.name)
        serializer = ShowSerializer(queryset)
        return response.Response(serializer.data)

class SeasonNestedViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = SeasonSerializer
    queryset = Season.objects.all()
    resource_name = "seasons"
    permission_classes = ()
    lookup_kwargs = {"pk": "id"}
    parent_lookup_kwargs = {"show_pk": "show_id"}

    def get_parent_object(self):
        return Show.objects.get(id=self.kwargs["show_pk"])

    def get_object(self):
        return Season.objects.get(id=self.kwargs["pk"])

    def list(self, request, *args, **kwargs):
        try:
            show = self.get_parent_object()
        except (Show.DoesNotExist):
            return response.Response(
                {"not_found": "Show not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        queryset = self.queryset.filter(show_id=show.id)
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        try:
            show = self.get_parent_object()
            queryset = self.queryset.get(season_number=self.kwargs["pk"], show=show)
            serializer = self.get_serializer(queryset)
        except (Season.DoesNotExist, Episode.DoesNotExist):
            return response.Response(
                {"not_found": "Show or Season not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        return response.Response(serializer.data)


class EpisodeNestedViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = EpisodeSerializer
    queryset = Episode.objects.all()
    resource_name = "episodes"
    permission_classes = ()
    lookup_kwargs = {"pk": "id"}
    parent_lookup_kwargs = {"season_pk": "season_id"}

    def get_parent_object(self):
        return Season.objects.get(
            season_number=self.kwargs["season_pk"], show=self.kwargs["show_pk"]
        )

    def get_object(self):
        return Episode.objects.get(id=self.kwargs["pk"])

    def list(self, request, *args, **kwargs):
        try:
            season = self.get_parent_object()
        except (Season.DoesNotExist):
            return response.Response(
                {"not_found": "Season not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        queryset = self.queryset.filter(season_id=season.id)
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        try:
            season = self.get_parent_object()
            queryset = self.queryset.get(
                episode_number=self.kwargs["pk"], season=season
            )
            serializer = self.get_serializer(queryset)

        except (Season.DoesNotExist, Episode.DoesNotExist):
            return response.Response(
                {"not_found": "Season or Episode not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return response.Response(serializer.data)


class EpisodeViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = EpisodeSerializer
    queryset = Episode.objects.all()
    resource_name = "episodes"
    permission_classes = ()


class SeasonViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = SeasonSerializer
    queryset = Season.objects.all()
    resource_name = "seasons"
    permission_classes = ()
