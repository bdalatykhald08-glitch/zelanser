from rest_framework import permissions


class IsClient(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and getattr(request.user, 'role', None) == 'client'


class IsFreelancer(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and getattr(request.user, 'role', None) == 'freelancer'


class IsAdminOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser)








