from .models import Thesis, Patent, Scholarship, Prize, Fund, Honor
from rest_framework import serializers, fields


class ThesisSerializers(serializers.ModelSerializer):
    """
    论文序列化器
    """
    class Meta:
        model = Thesis
        fields = ('id', "ths_stu", "ths_subject_code", "ths_subject", "ths_title")
        read_only_fields = ('id',)
        extra_kwargs = {
            'id': {
                'help_text': 'id'
            },
            'ths_stu': {
                'help_text': '学生'
            },
            'ths_subject_code': {
                'help_text': '所属学科代码'
            },
            'ths_subject': {
                'help_text': '所属学科名称'
            },
            'ths_title': {
                'help_text': '论文题目'
            },
        }


class PatentSerializers(serializers.ModelSerializer):
    """
    专利序列化器
    """
    class Meta:
        model = Patent
        fields = (
            "id", "pat_stu", "pat_type", "pat_loc", "pat_name", "pat_owner", "pat_code", "pat_date", "pat_join_count",
            "pat_apply", "pat_apply_info", "pat_group")
        read_only_fields = ('id',)
        extra_kwargs = {
            'pat_stu': {
                'help_text': '学生'
            },
            'pat_type': {
                'help_text': '专利类别'
            },
            'pat_loc': {
                'help_text': '专利授权国家(地区)'
            },
            'pat_name': {
                'help_text': '专利名称'
            },
            'pat_owner': {
                'help_text': '专利权人'
            },
            'pat_code': {
                'help_text': '专利号'
            },
            'pat_date': {
                'help_text': '授权公告日'
            },
            'pat_join_count': {
                'help_text': '本单位参与学科数'
            },
            'pat_apply': {
                'help_text': '专利转化形式'
            },
            'pat_apply_info': {
                'help_text': '转化或应用情况'
            },
            'pat_group': {
                'help_text': '专利权人数'
            },
        }


class AwardScholarshipSerializers(serializers.ModelSerializer):
    """
    奖学金序列化器
    """
    class Meta:
        model = Scholarship
        fields = ("id", "sch_stu", "sch_info", "sch_type", "sch_level", "sch_is_arrears")
        read_only_fields = ("id",)
        extra_kwargs = {
            'sch_stu': {
                'help_text': '学生'
            },
            'sch_info': {
                'help_text': '获奖情况和发表论文的情况'
            },
            'sch_type': {
                'help_text': '奖/助学金类型'
            },
            'sch_level': {
                'help_text': '初评等级'
            },
            'sch_is_arrears': {
                'help_text': '是否欠缴学费'
            },
        }


class PrizeSerializers(serializers.ModelSerializer):
    """
    获奖情况序列化器
    """
    class Meta:
        model = Prize
        fields = ("id", "pri_stu", "pri_name", "pri_project", "pri_level", "pri_unit", "pri_date", "pri_info")
        read_only_fields = ("id",)
        extra_kwargs = {
            'pri_stu': {
                'help_text': '学生'
            },
            'pri_name': {
                'help_text': '获奖名称'
            },
            'pri_project': {
                'help_text': '获奖项目'
            },
            'pri_level': {
                'help_text': '奖励等级'
            },
            'pri_unit': {
                'help_text': '颁奖单位'
            },
            'pri_date': {
                'help_text': '获奖时间'
            },
            'pri_info': {
                'help_text': '备注'
            },
        }


class FundSerializers(serializers.ModelSerializer):
    """
    专项资金序列化器
    """
    class Meta:
        model = Fund
        fields = (
            "id", "fund_stu", "fund_project_code", "fund_aca", "fund_leader", "fund_name", "fund_level", "fund_type",
            "fund_grade", "fund_money")
        read_only_fields = ("id",)
        extra_kwargs = {
            'fund_stu': {
                'help_text': '学生'
            },
            'fund_project_code': {
                'help_text': '项目编号'
            },
            'fund_aca': {
                'help_text': '学院'
            },
            'fund_leader': {
                'help_text': '负责人'
            },
            'fund_name': {
                'help_text': '项目名称'
            },
            'fund_level': {
                'help_text': '学历层次'
            },
            'fund_type': {
                'help_text': '学历类型'
            },
            'fund_grade': {
                'help_text': '级别'
            },
            'fund_money': {
                'help_text': '赞助金额'
            },
        }


class HonorSerializers(serializers.ModelSerializer):
    """
    荣誉称号序列化器
    """
    class Meta:
        model = Honor
        fields = ("id", "hon_stu", "hon_name", "hon_year", "hon_dep")
        read_only_fields = ("id",)
        extra_kwargs = {
            'hon_stu': {
                'help_text': '学生'
            },
            'hon_name': {
                'help_text': '荣誉称号名称'
            },
            'hon_year': {
                'help_text': '颁发年份'
            },
            'hon_dep': {
                'help_text': '颁发部门'
            },
        }
