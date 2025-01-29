from rest_framework import permissions

class IsCreatorOrSuperuserOrAdmin(permissions.BasePermission):
    """custom permission to allow only the creator of a user to view and modify that user account,
    except superusers who can access and modify all users accounts"""
    def has_object_permission(self, request, view, obj):
        # Superusers have full access
        if request.user.is_superuser or request.user.is_staff:
            return True

        # Only allow access if user is creator of list
        return obj == request.user