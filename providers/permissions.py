from rest_framework import permissions

class IsProviderOwner(permissions.BasePermission):
    """User can only access their own provider"""
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsAdminOrReadOnly(permissions.BasePermission):
    """Anyone can read; only admins can write"""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff