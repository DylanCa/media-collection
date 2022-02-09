from rest_framework import viewsets, status, response, mixins
from collection.games.api.serializers import GameSerializer, GenreSerializer, PlatformSerializer
from collection.games.models import Game, Genre, Platform

from collection.utils.filters import FilterViewSetMixin

class GameViewSet(FilterViewSetMixin, viewsets.ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all().order_by('id')
    resource_name = "games"
    permission_classes = ()


class PlatformViewSet(FilterViewSetMixin, viewsets.ModelViewSet):
    serializer_class = PlatformSerializer
    queryset = Platform.objects.all().order_by('id')
    resource_name = "platforms"
    permission_classes = ()

class GenreViewSet(FilterViewSetMixin, viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all().order_by('id')
    resource_name = "genres"
    permission_classes = ()
