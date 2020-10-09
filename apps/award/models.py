from django.db import models
from basic.models import Student


class Thesis(models.Model):
    """
    论文模型
    """
    ths_stu = models.ForeignKey(Student, verbose_name="学生", on_delete=models.CASCADE, null=True, blank=True)
    ths_subject_code = models.CharField(verbose_name="所属学科代码", max_length=128, null=True, blank=True)
    ths_subject = models.CharField(verbose_name="所属学科名称", max_length=128, null=True, blank=True)
    ths_title = models.CharField(verbose_name="论文题目", max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = "论文"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.ths_stu) + "-" + str(self.ths_title)


class Patent(models.Model):
    """
    专利模型
    """
    pat_stu = models.ForeignKey(Student, verbose_name="学生", on_delete=models.CASCADE, null=True, blank=True)
    pat_type = models.CharField(verbose_name="专利类别", max_length=128, null=True, blank=True)
    pat_loc = models.CharField(verbose_name="专利授权国家(地区)", max_length=128, null=True, blank=True)
    pat_name = models.CharField(verbose_name="专利名称", max_length=128, null=True, blank=True)
    pat_owner = models.CharField(verbose_name="专利权人", max_length=128, null=True, blank=True)
    pat_code = models.CharField(verbose_name="专利号", max_length=128, null=True, blank=True)
    pat_date = models.DateField(verbose_name="授权公告日", null=True, blank=True)
    pat_join_count = models.CharField(verbose_name="本单位参与学科数", max_length=128, null=True, blank=True)
    pat_apply = models.CharField(verbose_name="专利转化形式", max_length=128, null=True, blank=True)
    pat_apply_info = models.TextField(verbose_name="转化或应用情况", null=True, blank=True)
    pat_group = models.CharField(verbose_name="专利权人数", max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = "专利"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.pat_stu) + "-" + str(self.pat_name)


class Scholarship(models.Model):
    """
    奖/助学金模型
    """
    sch_stu = models.ForeignKey(Student, verbose_name="学生", on_delete=models.CASCADE, null=True, blank=True)
    sch_info = models.TextField(verbose_name="获奖情况和发表论文的情况", null=True, blank=True)
    sch_type = models.CharField(verbose_name="奖/助学金类型", max_length=128, null=True, blank=True)
    sch_level = models.CharField(verbose_name="初评等级", max_length=128, null=True, blank=True)
    sch_is_arrears = models.BooleanField(verbose_name="是否欠缴学费", default=False, null=True, blank=True)

    class Meta:
        verbose_name = "奖/助学金"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.sch_stu) + "-" + str(self.sch_type)


class Prize(models.Model):
    """
    获奖情况模型
    """
    pri_stu = models.ForeignKey(Student, verbose_name="学生", on_delete=models.CASCADE, null=True, blank=True)
    pri_name = models.CharField(verbose_name="获奖名称", max_length=128, null=True, blank=True)
    pri_project = models.CharField(verbose_name="获奖项目", max_length=128, null=True, blank=True)
    pri_level = models.CharField(verbose_name="奖励等级", max_length=128, null=True, blank=True)
    pri_unit = models.CharField(verbose_name="颁奖单位", max_length=128, null=True, blank=True)
    pri_date = models.DateField(verbose_name="获奖时间", null=True, blank=True)
    pri_info = models.TextField(verbose_name="备注", null=True, blank=True)

    class Meta:
        verbose_name = "获奖情况"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.pri_stu) + "-" + str(self.pri_name)


class Fund(models.Model):
    """
    专项资金模型
    """
    fund_stu = models.ForeignKey(Student, verbose_name="学生", on_delete=models.CASCADE, null=True, blank=True)
    fund_project_code = models.CharField(verbose_name="项目编号", max_length=128, null=True, blank=True)
    fund_aca = models.CharField(verbose_name="学院", max_length=128, null=True, blank=True)
    fund_leader = models.CharField(verbose_name="负责人", max_length=128, null=True, blank=True)
    fund_name = models.CharField(verbose_name="项目名称", max_length=128, null=True, blank=True)
    fund_level = models.CharField(verbose_name="学历层次", max_length=128, null=True, blank=True)
    fund_type = models.CharField(verbose_name="学位类型", max_length=128, null=True, blank=True)
    fund_grade = models.CharField(verbose_name="级别", max_length=128, null=True, blank=True)
    fund_money = models.CharField(verbose_name="赞助金额(元)", max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = "专项资金"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.fund_stu) + "-" + str(self.fund_name)


class Honor(models.Model):
    """
    荣誉称号模型
    """
    hon_stu = models.ForeignKey(Student, verbose_name="学生", on_delete=models.CASCADE, null=True, blank=True)
    hon_name = models.CharField(verbose_name="荣誉称号名称", max_length=128, null=True, blank=True)
    hon_year = models.CharField(verbose_name="颁发年份", max_length=128, null=True, blank=True)
    hon_dep = models.CharField(verbose_name="颁发部门", max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = "荣誉称号"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.hon_stu) + "-" + str(self.hon_name)
