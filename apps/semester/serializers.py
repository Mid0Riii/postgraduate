from rest_framework import serializers, fields, validators
from .models import Score, Departure, Semester


class ScoreSerializers(serializers.ModelSerializer):
    sem_name = serializers.ReadOnlyField(source='sco_sem.sem_name')

    class Meta:
        model = Score
        fields = ("sco_sem", 'sem_name', "sco_course", 'sco_score')
        extra_kwargs = {
            'sco_sem': {
                'help_text': '学期'
            },
            'sco_course': {
                'help_text': '课程'
            },
            'sco_stu': {
                'help_text': '学生'
            },
            'sco_score': {
                'help_text': '分数'
            },
        }


class DepartureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Departure
        fields = ('depart_stu', 'depart_type', 'depart_loc', 'depart_semster')
        # 联合唯一认证
        validators = [
            validators.UniqueTogetherValidator(
                queryset=Departure.objects.all(),
                fields=('depart_stu', 'depart_semster', "depart_type"),
                message="已经填写"
            ),
        ]

        extra_kwargs = {
            'depart_stu': {
                'help_text': '学生'
            },
            'depart_type': {
                'help_text': '记录类型'
            },
            'depart_datetime': {
                'help_text': '时间'
            },
            'depart_loc': {
                'help_text': '位置'
            },
            'depart_semster': {
                'help_text': '学期'
            },
        }

    def validate_depart_type(self, depart_type):
        s = Semester.objects.get(sem_is_available=True)
        if depart_type != s.sem_dep_status:
            raise serializers.ValidationError('无效的返校/离校类型')


class SemesterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ('sem_name', 'sem_dep_status',)
        read_only_fields = fields
        extra_kwargs = {
            'sem_name': {
                'help_text': '学期名'
            },
            'sem_dep_status': {
                'help_text': '离/返校状态'
            },
        }
