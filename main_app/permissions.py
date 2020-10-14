from rest_framework.permissions import BasePermission


class IsHrStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.profile.is_hr_staff
