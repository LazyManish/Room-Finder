from rest_framework import permissions


class IsAdminOnly(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.user.is_authenticated and request.user.role == 'seller':
            return True
        
        return False
    