from rest_framework.permissions import BasePermission, SAFE_METHODS
from basic.models import Student


class IsOwnerOrReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_permission(self, request, view):
        try:
            view.auth_field_name
        except Exception as e:
            raise PermissionError("缺乏auth_field_name字段")
        if request.method == 'POST':
            if view.auth_field_name in request.data:
                sid = Student.objects.get(stu_usr=request.user.id).id
                return sid == request.data[view.auth_field_name]
        return True

    def has_object_permission(self, request, view, obj):
        owner = getattr(obj, view.auth_field_name)
        visitor = Student.objects.get(stu_usr=request.user.id)
        if request.method in SAFE_METHODS:
            return owner == visitor
        else:
            if view.auth_field_name in request.data:
                sid = Student.objects.get(stu_usr=request.user.id).id
                return sid == request.data[view.auth_field_name]
            else:
                return True