from django_filters.rest_framework import DjangoFilterBackend

class FilterViewSetMixin():
    filter_backends = (DjangoFilterBackend,)

