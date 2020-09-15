from .models import Announcement
from rest_framework import serializers,fields

class AnnouncementSerializers(serializers.ModelSerializer):
    ann_file = fields.SerializerMethodField(label="文件")

    class Meta:
        model = Announcement
        fields = ('id','ann_title', 'ann_body','ann_file','ann_pubdate','ann_urgency')

    def get_ann_file(self,obj):
        """
        获取上传文件的绝对路径
        """
        file_list=[]
        for f in obj.ann_file.all():
            file_list.append(self.context['request'].build_absolute_uri(f.file_body.url))
        return file_list
