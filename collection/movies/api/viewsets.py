from rest_framework import viewsets, status, response, mixins
from collection.movies.api.serializers import CollectionSerializer, MovieSerializer

from collection.movies.models import Collection, Movie
from collection.utils.filters import FilterViewSetMixin


class MovieViewSet(FilterViewSetMixin, viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all().order_by('id')
    resource_name = "movies"
    permission_classes = ()


class CollectionViewSet(FilterViewSetMixin, viewsets.ModelViewSet):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all().order_by('id')
    resource_name = "collections"
    permission_classes = ()
