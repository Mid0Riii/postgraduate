from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets
from .serializers import AddressSerializers, PovertySerializers, StudentSerializers
from .models import Student, StudentClass, Poverty
from utils.mixins import FormatRetrieveModelMixin, FormatDestroyModelMixin, FormatUpdateModelMixin, \
    FormatListModelMixin, FormatResponse, SafeFormatCreateModelMixin
from utils.permissions import IsOwnerOrReadOnly

User = get_user_model()


class AddressBookViewset(viewsets.GenericViewSet, FormatListModelMixin):
    """
    list:获取登录用户通讯录
    """

    def get_queryset(self):
        user = self.request.user
        userclass = Student.objects.get(stu_usr=user).stu_class
        return Student.objects.filter(stu_class=userclass)

    serializer_class = AddressSerializers
    permission_classes = [permissions.IsAuthenticated, ]


class PovertyViewset(viewsets.GenericViewSet, FormatUpdateModelMixin, FormatListModelMixin):
    """
    list:获取登录用户填报的贫困生信息
    update:贫困生信息
    partial_update:局部修改贫困生信息
    """

    def get_queryset(self):
        user = self.request.user.id
        return Poverty.objects.filter(por_stu=user)

    serializer_class = PovertySerializers
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    auth_field_name = "por_stu"


class StudentViewset(viewsets.GenericViewSet, FormatListModelMixin):
    """
    list:获取登录用户的学生信息
    """

    def get_queryset(self):
        user = self.request.user.id
        return Student.objects.filter(stu_usr=user)

    serializer_class = StudentSerializers
    permission_classes = [permissions.IsAuthenticated]
