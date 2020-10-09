from .models import Announcement
from rest_framework import serializers, fields


class AnnouncementSerializers(serializers.ModelSerializer):
    ann_file = fields.SerializerMethodField(label="文件")

    class Meta:
        model = Announcement
        fields = ('id', 'ann_title', 'ann_body', 'ann_file', 'ann_pubdate', 'ann_urgency')
        extra_kwargs = {
            'id': {
                'help_text': 'id'
            },
            'ann_title': {
                'help_text': '公告标题'
            },
            'ann_body': {
                'help_text': '公告正文'
            },
            'ann_visibility': {
                'help_text': '是否可见'
            },
            'ann_file': {
                'help_text': '关联文件'
            },
            'ann_pubdate': {
                'help_text': '发布时间'
            },
            'ann_urgency': {
                'help_text': '紧急程度'
            },
        }

    def get_ann_file(self, obj):
        """
        获取上传文件的绝对路径
        """
        file_list = []
        for f in obj.ann_file.all():
            file = {
                "title": f.file_title,
                "url": self.context['request'].build_absolute_uri(f.file_body.url)
            }
            file_list.append(file)
        if file_list == []:
            file_list = None
        return file_list
