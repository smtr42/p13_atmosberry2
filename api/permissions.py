from rest_framework import permissions


class IsAuthor0rReaOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # read only perm for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # write perm is only allowed to the user
        return obj.user == request.user
