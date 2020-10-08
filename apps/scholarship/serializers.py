from rest_framework import serializers, fields
from .models import ScholarshipBasic, ScholarshipApply


class ScholarshipSerializers(serializers.ModelSerializer):
    class Meta:
        model = ScholarshipBasic
        fields = ('id', "sch_title", "sch_type", "sch_pub_date", "sch_is_available", "sch_info")
        read_only_fields = fields


class ApplySerializers(serializers.ModelSerializer):
    class Meta:
        model = ScholarshipApply
        fields = (
        'id', "app_sch", "app_stu", "app_tutor_score", "app_moral_score", "app_course_score", "app_academy_score",
        "app_social_score", "app_review_results", "app_general_score")
        read_only_fields = ("id", "app_review_results", "app_general_score")
