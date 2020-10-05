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
            file = {
                "title":f.file_title,
                "url":self.context['request'].build_absolute_uri(f.file_body.url)
            }
            file_list.append(file)
        if file_list ==[]:
            file_list=None
        return file_list
