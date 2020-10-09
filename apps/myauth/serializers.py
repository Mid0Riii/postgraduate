from .models import CustomUser
from rest_framework import serializers


class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username',)
    read_only_fields =['username']
    extra_kwargs={
        'username': {
            'help_text': '用户名'
        },
    }