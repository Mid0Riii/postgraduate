from rest_framework import generics, permissions, views, mixins, status, viewsets
from .serializers import ScholarshipSerializers, ApplySerializers
from .models import ScholarshipBasic, ScholarshipApply
from utils.drf import FormatResponse
from utils.mixins import FormatListModelMixin, SafeFormatCreateModelMixin, FormatRetrieveModelMixin, \
    FormatUpdateModelMixin, FormatDestroyModelMixin
from utils.permissions import IsOwnerOrReadOnly


class ScholarshipViewset(viewsets.GenericViewSet, FormatListModelMixin):
    """
    list:获取当前有效的奖学金项目信息
    """
    serializer_class = ScholarshipSerializers
    permission_classes = [permissions.IsAuthenticated]
    queryset = ScholarshipBasic.objects.all()


class ApplyViewset(viewsets.GenericViewSet, FormatListModelMixin, SafeFormatCreateModelMixin, FormatUpdateModelMixin,
                   FormatDestroyModelMixin, FormatRetrieveModelMixin):
    def get_queryset(self):
        return ScholarshipApply.objects.filter(app_stu__stu_usr=self.request.user.id).order_by('-id')
    """
    list:获取登录用户发起的奖学金申请
    create:创建新的奖学金申请
    read:获取奖学金申请详情
    update:修改奖学金申请
    partial_update:局部修改奖学金申请
    delete:删除奖学金申请
    """
    serializer_class = ApplySerializers
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    auth_field_name = "app_stu"
