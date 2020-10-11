from rest_framework import serializers, fields
from .models import ScholarshipBasic, ScholarshipApply


class ScholarshipSerializers(serializers.ModelSerializer):
    class Meta:
        model = ScholarshipBasic
        fields = ('id', "sch_title", "sch_type", "sch_pub_date", "sch_is_available", "sch_info")
        read_only_fields = fields
        extra_kwargs={
            'id': {
                'help_text': 'id'
            },
            'sch_title': {
                'help_text': '奖学金标题'
            },
            'sch_type': {
                'help_text': '奖学金类型'
            },
            'sch_is_available': {
                'help_text': '评选是否开始'
            },
            'sch_pub_date': {
                'help_text': '发布时间'
            },
            'sch_info': {
                'help_text': '备注'
            },
        }


class ApplySerializers(serializers.ModelSerializer):
    sch_title = fields.SerializerMethodField(label="奖学金名")

    def get_sch_title(self,obj):
        """
        获取奖学金id对应奖学金名
        """
        if obj.app_sch!=None:
            return obj.app_sch.sch_title
        else:
            return None

    class Meta:
        model = ScholarshipApply
        fields = (
        'id', "app_sch", "app_stu",'sch_title', "app_tutor_score", "app_moral_score", "app_course_score", "app_academy_score",
        "app_social_score", "app_review_results", "app_general_score")
        read_only_fields = ("id", "app_review_results", "app_general_score")
        extra_kwargs = {
            'id': {
                'help_text': 'id'
            },
            'app_sch': {
                'help_text': '申请奖学金项目'
            },
            'app_stu': {
                'help_text': '申请人'
            },
            'app_tutor_score': {
                'help_text': '导师考核得分'
            },
            'app_moral_score': {
                'help_text': '思想品德得分'
            },
            'app_course_score': {
                'help_text': '课业成绩得分'
            },
            'app_academy_score': {
                'help_text': '学术表现得分'
            },
            'app_social_score': {
                'help_text': '社会活动得分'
            },
            'app_review_results': {
                'help_text': '审核结果'
            },
            'app_general_score': {
                'help_text': '综合得分'
            },
        }