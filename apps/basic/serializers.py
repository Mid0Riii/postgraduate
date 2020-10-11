from .models import StudentClass, Student, Poverty
from rest_framework import serializers, fields


class AddressSerializers(serializers.ModelSerializer):
    stu_class = fields.SerializerMethodField()
    def get_stu_class(self,obj):
        return obj.stu_class.cls_name
    class Meta:
        model = Student
        fields = ('id','stu_id','stu_class', 'stu_name', 'stu_tel', 'stu_birth')
        extra_kwargs={
            'id': {
                'help_text': 'id'
            },
            'stu_id': {
                'help_text': '学号'
            },
            'stu_name': {
                'help_text': '姓名'
            },
            'stu_tel': {
                'help_text': '联系方式'
            },
            'stu_birth': {
                'help_text': '出生日期'
            },
            'stu_class': {
                'help_text': '班级'
            },
        }

class PovertySerializers(serializers.ModelSerializer):
    class Meta:
        model = Poverty
        fields = ('id',"por_stu", "por_tel", "por_family1", "por_family1_tel", "por_family1_job", "por_family2",
                  "por_family2_tel", "por_family2_job", "por_is_archived", "por_info")
        read_only_fields = ("id","por_stu",)
        extra_kwargs = {
            'id': {
                'help_text': 'id'
            },
            'por_stu': {
                'help_text': '学生'
            },
            'por_tel': {
                'help_text': '联系方式'
            },
            'por_family1': {
                'help_text': '家庭成员1'
            },
            'por_family1_tel': {
                'help_text': '联系电话1'
            },
            'por_family1_job': {
                'help_text': '家庭成员1工作单位'
            },
            'por_family2': {
                'help_text': '家庭成员2'
            },
            'por_family2_tel': {
                'help_text': '家庭成员2联系电话'
            },
            'por_family2_job': {
                'help_text': '家庭成员2工作单位'
            },
            'por_is_archived': {
                'help_text': '是否为建档立卡户'
            },
            'por_info': {
                'help_text': '家庭主要情况'
            },
        }

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','stu_usr','stu_id','stu_name','stu_college','stu_major')
        read_only_fields = ('id','stu_usr','stu_id')
        extra_kwargs = {
            'id': {
                'help_text': 'id'
            },
            'stu_usr': {
                'help_text': '关联用户id'
            },
            'stu_id': {
                'help_text': '学号'
            },
            'stu_name': {
                'help_text': '姓名'
            },
            'stu_college': {
                'help_text': '学院'
            },
            'stu_major': {
                'help_text': '专业'
            },
        }