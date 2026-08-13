from rest_framework.permissions import SAFE_METHODS, BasePermission


from accounts.models import User


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        user: User = request.user
        return user.is_authenticated and user.is_superuser

class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
        


    def has_object_permission(self, request, view, obj):
        return request.user == obj.user or request.user.is_superuser