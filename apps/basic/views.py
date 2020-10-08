from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets
from .serializers import AddressSerializers, PovertySerializers
from .models import Student, StudentClass, Poverty
from utils.mixins import FormatRetrieveModelMixin, FormatDestroyModelMixin, FormatUpdateModelMixin, \
    FormatListModelMixin, FormatResponse, SafeFormatCreateModelMixin
from utils.permissions import IsOwnerOrReadOnly

User = get_user_model()


class AddressBookViewset(viewsets.GenericViewSet, FormatListModelMixin):
    def get_queryset(self):
        user = self.request.user
        userclass = Student.objects.get(stu_usr=user).stu_class
        return Student.objects.filter(stu_class=userclass)

    serializer_class = AddressSerializers
    permission_classes = [permissions.IsAuthenticated, ]


class PovertyViewset(viewsets.GenericViewSet, FormatRetrieveModelMixin, FormatUpdateModelMixin, FormatListModelMixin):
    def get_queryset(self):
        user = self.request.user.id
        return Poverty.objects.filter(por_stu=user)

    serializer_class = PovertySerializers
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    auth_field_name = "por_stu"
