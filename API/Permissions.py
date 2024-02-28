from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS


class IsOwnerPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_superuser)



class IsOwnerObjPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request in SAFE_METHODS:
            return True
        else:
            return bool(request.user.is_superuser or obj.author == request.user)
