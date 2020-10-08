from django.db import models
from basic.models import Student, StudentClass
from utils.modeltool import set_choices
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Semester(models.Model):
    sem_name = models.CharField(verbose_name="学期名", max_length=128, null=True, blank=True)
    sem_is_available = models.BooleanField(verbose_name="是否为当前学期", default=False, null=True)
    sem_dep_status = models.CharField(max_length=5, verbose_name="离/返校状态", choices=set_choices(["离校", "返校", "关闭统计"]),
                                      default="关闭统计")

    class Meta:
        verbose_name = "学期"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sem_name

    def clean(self):
        if self.sem_is_available:
            qs = Semester.objects.all()
            for q in qs:
                if q.sem_is_available:
                    msg = ("当前已有一个学期({name})处在激活状态，在激活其他学期之前，必须将上个学期关闭").format(name=q.sem_name)
                    raise ValidationError(_(msg))


class Departure(models.Model):
    depart_stu = models.ForeignKey(Student, verbose_name="学生", on_delete=models.CASCADE, null=True, blank=True)
    depart_type = models.CharField(verbose_name="记录类型", max_length=128, choices=set_choices(['离校', '返校']), null=True,
                                   blank=True)
    depart_datetime = models.DateTimeField(verbose_name="时间", auto_now_add=True)
    depart_loc = models.CharField(verbose_name="位置", max_length=128, null=True, blank=True)
    depart_semster = models.ForeignKey(Semester, verbose_name="学期", on_delete=models.CASCADE, null=True,
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
        verbose_name = "成绩"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.sco_stu.stu_name) + '-' + str(self.sco_sem) + '-' + str(self.sco_course)
