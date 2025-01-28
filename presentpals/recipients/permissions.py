from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.list == request.user

class IsCreatorOrSuperuser(permissions.BasePermission):
    """custom permission to allow only the creator of a list to view and modify recipients on it,
    except superusers who can access and modify all lists"""
    def has_object_permission(self, request, view, obj):
        # Superusers have full access
        if request.user.is_superuser:
            return True

        # Only allow access if user is creator of list
        print('owner ', obj.list.owner)
        print('user ', request.user)
        return obj.list.owner == request.user