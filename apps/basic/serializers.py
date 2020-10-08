from .models import StudentClass, Student, Poverty
from rest_framework import serializers, fields


class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','stu_id', 'stu_name', 'stu_tel', 'stu_birth')


class PovertySerializers(serializers.ModelSerializer):
    class Meta:
        model = Poverty
        fields = ('id',"por_stu", "por_tel", "por_family1", "por_family1_tel", "por_family1_job", "por_family2",
                  "por_family2_tel", "por_family2_job", "por_is_archived", "por_info")
        read_only_fields = ("id","por_stu",)
