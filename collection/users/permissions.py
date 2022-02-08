from rest_framework import permissions

from collection.users.models import User

class IsOwner(permissions.BasePermission):
     def has_permission(self, request, view):
        return request.user == User.objects.get(id=view.kwargs['user_pk'])