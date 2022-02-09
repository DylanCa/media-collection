from django_filters.rest_framework import DjangoFilterBackend

class FilterViewSetMixin():
    filter_backends = (DjangoFilterBackend,)

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)

        title = self.request.query_params.get('title', None)
        if title:
            queryset = queryset.filter(title__icontains=title)

        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name__icontains=name)

        resource_type = self.request.query_params.get('resource_type', None)
        if resource_type:
            queryset = queryset.filter(resource_type__model__icontains=resource_type)
        
        username = self.request.query_params.get('username', None)
        if username:
            queryset = queryset.filter(username__icontains=username)

        return queryset
