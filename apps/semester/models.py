from django.db import models
from basic.models import Student, StudentClass
from utils.modeltool import set_choices


# Create your models here.

class Semester(models.Model):
    sem_name = models.CharField(verbose_name="学期名", max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = "学期管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sem_name


class DepartControl(models.Model):
    # TODO 增加表单验证逻辑，确保不会有多个离校/返校同时启动
    depc_sem = models.OneToOneField(Semester, verbose_name="学期名", on_delete=models.CASCADE, null=True, blank=True)
    depc_dep_avai = models.BooleanField(verbose_name="是否开始离校", null=True, blank=True, default=False)
    depc_arr_avai = models.BooleanField(verbose_name="是否开始返校", null=True, blank=True, default=False)

    class Meta:
        verbose_name = "离/返校控制"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.depc_sem)


class Departure(models.Model):
    depart_stu = models.ForeignKey(Student, verbose_name="学生", on_delete=models.CASCADE, null=True, blank=True)
    depart_type = models.CharField(verbose_name="记录类型", max_length=128, choices=set_choices(['离校', '返校']), null=True,
                                   blank=True)
    depart_datetime = models.DateTimeField(verbose_name="时间", auto_now_add=True)
    depart_loc = models.CharField(verbose_name="位置", max_length=128, null=True, blank=True)
    depart_semster = models.ForeignKey(DepartControl, verbose_name="学期", on_delete=models.CASCADE, null=True,
                                       blank=True)

    class Meta:
        verbose_name = "离/返校信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.depart_semster) + "-" + str(self.depart_stu) + "-" + str(self.depart_type)

    def get_class(self):
        return self.depart_stu.stu_class

    get_class.allow_tags = False
    get_class.short_description = ("班级")


class Score(models.Model):
    sco_cls = models.ForeignKey(StudentClass, verbose_name="班级", on_delete=models.CASCADE, null=True, blank=True)
    sco_sem = models.ForeignKey(Semester, verbose_name="学期", on_delete=models.CASCADE, null=True, blank=True)
    sco_course = models.CharField(verbose_name="课程", max_length=128, null=True, blank=True)
    sco_stu = models.ForeignKey(Student, verbose_name="学生", on_delete=models.CASCADE, null=True, blank=True)
    sco_score = models.CharField(verbose_name="分数", max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = "成绩录入"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.sco_stu.stu_name) + '-' + str(self.sco_sem) + '-' + str(self.sco_course)
