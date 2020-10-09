from .serializers import ThesisSerializers, AwardScholarshipSerializers, FundSerializers, HonorSerializers, \
    PatentSerializers, PrizeSerializers
from rest_framework import permissions, viewsets
from .models import Thesis, Patent, Scholarship, Prize, Honor, Fund
from utils.mixins import SafeFormatCreateModelMixin, FormatListModelMixin, FormatRetrieveModelMixin, \
    FormatUpdateModelMixin, FormatDestroyModelMixin
from utils.permissions import IsOwnerOrReadOnly


class AwardBaseViewset(viewsets.GenericViewSet, SafeFormatCreateModelMixin, FormatListModelMixin,
                       FormatUpdateModelMixin,
                       FormatDestroyModelMixin, FormatRetrieveModelMixin):
    """
    获奖情况基类，除GenericViewSet外均继承自utils.mixins中的自定义mixin
    """
    # 权限设置为仅自己可写
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class ThesisViewset(AwardBaseViewset):
    """
    list:获取登录用户填报的历史论文信息
    create:为当前用户增加论文信息
    read:获取论文详情
    update:修改历史论文信息
    partial_update:局部修改历史论文信息
    delete:删除历史论文信息
    """

    def get_queryset(self):
        return Thesis.objects.filter(ths_stu__stu_usr=self.request.user.id)

    serializer_class = ThesisSerializers
    auth_field_name = "ths_stu"


class PatentListViewsets(AwardBaseViewset):
    """
    list:获取登录用户填报的历史专利信息
    create:为当前用户增加专利信息
    read:获取专利详情
    update:修改历史专利信息
    partial_update:局部修改历史专利信息
    delete:删除历史专利信息
    """
    def get_queryset(self):
        return Patent.objects.filter(pat_stu__stu_usr=self.request.user.id)

    serializer_class = PatentSerializers
    auth_field_name = "pat_stu"


class ScholarshipViewset(AwardBaseViewset):
    """
    list:获取登录用户填报的历史奖学金情况信息
    create:为当前用户增加奖学金信息
    read:获取奖学金详情
    update:修改历史奖学金信息
    partial_update:局部修改历史奖学金信息
    delete:删除历史奖学金信息
    """
    def get_queryset(self):
        return Scholarship.objects.filter(sch_stu__stu_usr=self.request.user.id)

    serializer_class = AwardScholarshipSerializers
    auth_field_name = "sch_stu"


class PrizeViewset(AwardBaseViewset):
    """
    list:获取登录用户填报的历史获奖情况信息
    create:为当前用户增加获奖情况信息
    read:获取获奖情况详情
    update:修改历史获奖情况信息
    partial_update:局部修改历史获奖情况信息
    delete:删除历史获奖情况信息
    """
    def get_queryset(self):
        return Prize.objects.filter(pri_stu__stu_usr=self.request.user.id)

    serializer_class = PrizeSerializers
    auth_field_name = "pri_stu"


class FundViewset(AwardBaseViewset):
    """
    list:获取登录用户填报的历史专项资金信息
    create:为当前用户增加专项资金信息
    read:获取专项资金详情
    update:修改历史专项资金信息
    partial_update:局部修改历史专项资金信息
    delete:删除历史专项资金信息
    """
    def get_queryset(self):
        return Fund.objects.filter(fund_stu__stu_usr=self.request.user.id)

    serializer_class = FundSerializers
    auth_field_name = "fund_stu"


class HonorViewset(AwardBaseViewset):
    """
    list:获取登录用户填报的历史荣誉称号信息
    create:为当前用户增加荣誉称号信息
    read:获取荣誉称号详情
    update:修改历史荣誉称号信息
    partial_update:局部修改历史荣誉称号信息
    delete:删除历史荣誉称号信息
    """
    def get_queryset(self):
        return Honor.objects.filter(hon_stu__stu_usr=self.request.user.id)

    serializer_class = HonorSerializers
    auth_field_name = "hon_stu"
