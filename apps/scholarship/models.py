from django.db import models
from utils.modeltool import set_choices
from basic.models import StudentClass, Student


# Create your models here.

class ScholarshipBasic(models.Model):
    sch_title = models.CharField(verbose_name="奖学金标题", max_length=128, null=True, blank=True)
    sch_type = models.CharField(verbose_name="奖学金类型", max_length=128,
                                choices=set_choices(['国家奖学金', '省政府奖学金', '学业奖学金', '优秀奖学金']))
    sch_is_available = models.BooleanField(verbose_name="评选是否开始", default=False)
    sch_pub_date = models.DateField(verbose_name="发布时间", auto_now_add=True)
    sch_info = models.TextField(verbose_name="备注",null=True,blank=True)

    class Meta:
        verbose_name = "奖学金管理"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.sch_title


class ScholarshipApply(models.Model):
    app_sch = models.ForeignKey(ScholarshipBasic, verbose_name="申请奖学金项目", null=True, blank=True,
                                on_delete=models.CASCADE)
    app_stu = models.ForeignKey(Student, verbose_name="申请人", on_delete=models.CASCADE, null=True, blank=True)
    app_tutor_score = models.FloatField(verbose_name="导师考核得分", null=True, blank=True)
    app_moral_score = models.FloatField(verbose_name="思想品德得分", null=True, blank=True)
    app_course_score = models.FloatField(verbose_name="课业成绩得分", null=True, blank=True)
    app_academy_score = models.FloatField(verbose_name="学术表现得分", null=True,
                                          blank=True)
    app_social_score = models.FloatField(verbose_name="社会活动得分", null=True, blank=True)
    app_review_results = models.CharField(verbose_name="审核结果", max_length=128,
                                          choices=set_choices(['未审核', '审核通过', '审核驳回']),
                                          default='未审核')
    app_general_score = models.FloatField(verbose_name="综合得分", default='0')

    class Meta:
        verbose_name = "奖学金申请"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return str(self.app_stu) + '-' + str(self.app_sch)

    def save(self, *args, **kwargs):
        if self.app_review_results == "审核通过":
            general = self.app_tutor_score * 0.05 + self.app_moral_score * 0.05 + self.app_course_score * 0.1 + self.app_academy_score * 0.75 + self.app_social_score * 0.05
            self.app_general_score = general
        else:
            self.app_general_score = 0
        super().save(*args, **kwargs)
