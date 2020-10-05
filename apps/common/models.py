from django.db import models
from utils import modeltool
# Create your models here.

class Announcement(models.Model):
    ann_title = models.CharField(verbose_name="公告标题", max_length=128, null=True, blank=True)
    ann_body = models.TextField(verbose_name="公告正文", null=True, blank=True)
    ann_visibility = models.BooleanField(verbose_name="是否可见", default=False)
    ann_file = models.ManyToManyField('MyFile', verbose_name="关联文件", blank=True)
    ann_pubdate = models.DateField(verbose_name="发布时间",auto_now=True,null=True,blank=True)
    ann_urgency = models.IntegerField(verbose_name="紧急程度",choices=([3,'普通'],[2,'紧急'],[1,'置顶']),default="一般")

    class Meta:
        verbose_name = "公告发布"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ann_title


class Tag(models.Model):
    tag_name = models.CharField(verbose_name="标签名", max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = "标签管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag_name


class MyFile(models.Model):
    file_title = models.CharField(verbose_name="文件名", max_length=128, null=True, blank=True)
    file_body = models.FileField(verbose_name="文件", null=True, blank=True,upload_to="ann_files")
    file_tag = models.ManyToManyField(Tag, verbose_name="标签", blank=True)

    class Meta:
        verbose_name = "文件管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.file_title
