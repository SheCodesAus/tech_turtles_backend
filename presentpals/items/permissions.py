from rest_framework import permissions

class IsCreatorOrSuperuserOrAdmin(permissions.BasePermission):
    """custom permission to allow only the creator of a list to view and modify recipients on it,
    except superusers who can access and modify all lists"""
    def has_object_permission(self, request, view, obj):
        # Superusers have full access
        if request.user.is_superuser or request.user.is_staff:
            return True

        # Only allow access if user is creator of list
        return obj.recipient.list.owner == request.user