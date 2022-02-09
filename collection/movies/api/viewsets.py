from rest_framework import viewsets, status, response, mixins
from collection.movies.api.serializers import CollectionSerializer, MovieSerializer

from collection.movies.models import Collection, Movie


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    resource_name = "movies"
    permission_classes = ()


class CollectionViewSet(viewsets.ModelViewSet):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    resource_name = "collections"
    permission_classes = ()
