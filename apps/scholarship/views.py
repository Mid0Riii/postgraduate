from rest_framework import generics, permissions, views, mixins, status, viewsets
from .serializers import ScholarshipSerializers, ApplySerializers
from .models import ScholarshipBasic, ScholarshipApply
from utils.drf import FormatResponse
from utils.mixins import FormatListModelMixin, SafeFormatCreateModelMixin, FormatRetrieveModelMixin, \
    FormatUpdateModelMixin, FormatDestroyModelMixin
from utils.permissions import IsOwnerOrReadOnly


class ScholarshipViewset(viewsets.GenericViewSet, FormatListModelMixin):
    serializer_class = ScholarshipSerializers
    permission_classes = [permissions.IsAuthenticated]
    queryset = ScholarshipBasic.objects.all()


class ApplyViewset(viewsets.GenericViewSet, FormatListModelMixin, SafeFormatCreateModelMixin, FormatUpdateModelMixin,
                   FormatDestroyModelMixin, FormatRetrieveModelMixin):
    def get_queryset(self):
        return ScholarshipApply.objects.filter(app_stu__stu_usr=self.request.user.id)

    serializer_class = ApplySerializers
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    auth_field_name = "app_stu"
