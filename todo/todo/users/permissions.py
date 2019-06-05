from rest_framework.permissions import BasePermission

from todo.core.permissions import IsAllowedMethodOrStaff


class CustomIsAllowedMethodOrStaff(IsAllowedMethodOrStaff):
    methods = ['GET', 'HEAD', 'OPTIONS', 'PATCH']


class IsCurrentUserOrStaff(BasePermission):

    def has_object_permission(self, request, view, obj):
        return True if request.user.is_staff else request.user == obj
