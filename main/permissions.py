from rest_framework.permissions import BasePermission

class IsModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name__exact="Moderator").exists()

class NotModerator(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name__exact="Moderator").exists():
            return False
        else:
            return True
class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


