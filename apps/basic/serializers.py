from .models import StudentClass,Student
from rest_framework import serializers,fields

class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('stu_id','stu_name','stu_tel','stu_birth')