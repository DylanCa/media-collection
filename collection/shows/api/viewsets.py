from rest_framework import viewsets, status, response
from rest_framework_nested.viewsets import NestedViewSetMixin

from collection.shows.api.serializers import EpisodeSerializer, SeasonSerializer, ShowSerializer
from ..models import Show, Season, Episode

class ShowViewSet(viewsets.ModelViewSet):
    serializer_class = ShowSerializer
    queryset = Show.objects.all()
    resource_name = 'shows'
    permission_classes = ()

class SeasonViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = SeasonSerializer
    queryset = Season.objects.all()
    resource_name = 'seasons'
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
            season = self.get_object()
        except (Season.DoesNotExist, Episode.DoesNotExist):
            return response.Response(
                {"not_found": "Show or Season not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        if season.show == show:
            return super().retrieve(request, *args, **kwargs)
        else:
            return response.Response(
                {"not_found": "Season not found in this Show."},
                status=status.HTTP_404_NOT_FOUND,
            )

