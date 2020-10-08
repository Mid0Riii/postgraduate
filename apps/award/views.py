from django.shortcuts import render
from .serializers import ThesisSerializers, ScholarshipSerializers, FundSerializers, HonorSerializers, \
    PatentSerializers, PrizeSerializers
from rest_framework import generics, permissions, viewsets, status, mixins
from .models import Thesis, Patent, Scholarship, Prize, Honor, Fund
from utils.drf import FormatResponse
from utils.mixins import SafeFormatCreateModelMixin, FormatListModelMixin, FormatRetrieveModelMixin, \
    FormatUpdateModelMixin, FormatDestroyModelMixin
from utils.permissions import IsOwnerOrReadOnly


class AwardBaseViewset(viewsets.GenericViewSet, SafeFormatCreateModelMixin, FormatListModelMixin,
                       FormatUpdateModelMixin,
                       FormatDestroyModelMixin, FormatRetrieveModelMixin):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class ThesisViewset(AwardBaseViewset):

    def get_queryset(self):
        return Thesis.objects.filter(ths_stu__stu_usr=self.request.user.id)

    serializer_class = ThesisSerializers
    auth_field_name = "ths_stu"


class PatentListViewsets(AwardBaseViewset):

    def get_queryset(self):
        return Patent.objects.filter(pat_stu__stu_usr=self.request.user.id)

    serializer_class = PatentSerializers
    auth_field_name = "pat_stu"


class ScholarshipViewset(AwardBaseViewset):
    def get_queryset(self):
        return Scholarship.objects.filter(sch_stu__stu_usr=self.request.user.id)

    serializer_class = ScholarshipSerializers
    auth_field_name = "sch_stu"


class PrizeViewset(AwardBaseViewset):
    def get_queryset(self):
        return Prize.objects.filter(pri_stu__stu_usr=self.request.user.id)

    serializer_class = PrizeSerializers
    auth_field_name = "pri_stu"


class FundViewset(AwardBaseViewset):
    def get_queryset(self):
        return Fund.objects.filter(fund_stu__stu_usr=self.request.user.id)

    serializer_class = FundSerializers
    auth_field_name = "fund_stu"


class HonorViewset(AwardBaseViewset):
    def get_queryset(self):
        return Honor.objects.filter(hon_stu__stu_usr=self.request.user.id)

    serializer_class = HonorSerializers
    auth_field_name = "hon_stu"
