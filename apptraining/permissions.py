from rest_framework.permissions import BasePermission
from users.models import UserRoles


class IsOwnerOrStaff(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return request.user == view.get_object().owner

class IsModerator(BasePermission):
    """Пользователь из группы MODERATOR"""
    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user




class IsMember(BasePermission):
    """Пользователь из группы MEMBER"""
    def has_permission(self, request, view):
        if request.user.role == UserRoles.MEMBER:
            return True
        return False