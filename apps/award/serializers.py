from .models import Thesis, Patent, Scholarship, Prize, Fund, Honor
from rest_framework import serializers, fields


class ThesisSerializers(serializers.ModelSerializer):
    class Meta:
        model = Thesis
        fields = ('id', "ths_stu", "ths_subject_code", "ths_subject", "ths_title")
        read_only_fields = ('id',)


class PatentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patent
        fields = (
            "id", "pat_stu", "pat_type", "pat_loc", "pat_name", "pat_owner", "pat_code", "pat_date", "pat_join_count",
            "pat_apply", "pat_apply_info", "pat_group")
        read_only_fields = ('id',)


class ScholarshipSerializers(serializers.ModelSerializer):
    class Meta:
        model = Scholarship
        fields = ("id", "sch_stu", "sch_info", "sch_type", "sch_level", "sch_is_arrears")
        read_only_fields = ("id",)


class PrizeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Prize
        fields = ("id", "pri_stu", "pri_name", "pri_project", "pri_level", "pri_unit", "pri_date", "pri_info")
        read_only_fields = ("id",)


class FundSerializers(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = (
            "id", "fund_stu", "fund_project_code", "fund_aca", "fund_leader", "fund_name", "fund_level", "fund_type",
            "fund_grade", "fund_money")
        read_only_fields = ("id",)


class HonorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Honor
        fields = ("id", "hon_stu", "hon_name", "hon_year", "hon_dep")
        read_only_fields = ("id",)
