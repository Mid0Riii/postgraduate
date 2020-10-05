from django.db import models
from utils.modeltool import set_choices
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

class StudentClass(models.Model):
    """
    班级信息
    """
    cls_name = models.CharField(verbose_name="班名", max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = "班级信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cls_name


class Tutor(models.Model):
    """
    导师信息
    """
    tut_name = models.CharField(verbose_name="姓名", max_length=128, null=True, blank=True)
    tut_communication = models.CharField(verbose_name="导师联系方式", max_length=128, null=True, blank=True)
    tut_dorm = models.CharField(verbose_name="导师楼栋号", max_length=128, null=True, blank=True)
    tut_loc = models.CharField(verbose_name="家庭住址", max_length=128, null=True, blank=True)
    tut_fam = models.CharField(verbose_name="家庭成员", max_length=128, null=True, blank=True)
    tut_fam_tel = models.CharField(verbose_name="家庭成员联系方式", max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = "导师信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tut_name


class Student(models.Model):
    """
    学生信息
    """
    stu_usr = models.OneToOneField(User,verbose_name="关联用户",on_delete=models.CASCADE)
    stu_id = models.CharField(verbose_name="学号", max_length=128, null=True, blank=True)
    stu_name = models.CharField(verbose_name="姓名", max_length=128, null=True, blank=True)
    stu_college = models.CharField(verbose_name="学院", max_length=128, null=True, blank=True)
    stu_class = models.ForeignKey(StudentClass, verbose_name="班级", on_delete=models.CASCADE, null=True, blank=True)
    stu_major = models.CharField(verbose_name="专业", max_length=128, null=True, blank=True)
    stu_gender = models.CharField(verbose_name="性别", max_length=128, null=True, blank=True)
    stu_birth = models.DateField(verbose_name="出生年月", null=True, blank=True)
    stu_identity = models.CharField(verbose_name="身份证号", max_length=128, null=True, blank=True)
    stu_political_status = models.CharField(verbose_name="政治面貌", max_length=128, choices=set_choices(
        ['中共党员', '中共预备党员', '共青团员',
         '民革党员', '民盟党员', '民建会员',
         '民进会员', '农工党党员', '致公党党员',
         '九三学社社员', '台盟盟员', '无党派人士', '群众']), null=True, blank=True)
    stu_folk = models.CharField(verbose_name="民族", max_length=128, null=True, blank=True)
    stu_tel = models.CharField(verbose_name="联系方式", max_length=128, null=True, blank=True)
    stu_graduate = models.CharField(verbose_name="本科毕业院校", max_length=128, null=True, blank=True)
    stu_location = models.CharField(verbose_name="生源所在地", max_length=128, null=True, blank=True)
    stu_direction = models.CharField(verbose_name="专业方向", max_length=128, null=True, blank=True)
    stu_tutor = models.ForeignKey(Tutor, verbose_name="导师", on_delete=models.CASCADE, max_length=128, null=True,
                                  blank=True)

    class Meta:
        verbose_name = "学生信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.stu_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # from employ.models import Employment
        Employment.objects.update_or_create(emp_stu=self, emp_id=self.stu_id, emp_gender=self.stu_gender,
                                            emp_loc=self.stu_location)
        Poverty.objects.update_or_create(por_stu=self,por_id=self.stu_id,por_tel = self.stu_tel)


class Employment(models.Model):
    """
    就业信息
    """
    emp_stu = models.OneToOneField(Student, on_delete=models.CASCADE, verbose_name="学生", null=True, blank=True,
                                   unique=True)
    emp_id = models.CharField(verbose_name="学号", max_length=128, null=True, blank=True)
    emp_gender = models.CharField(verbose_name="性别", max_length=128, null=True, blank=True)
    emp_loc = models.CharField(verbose_name="生源地", max_length=128, null=True, blank=True)
    emp_type = models.CharField(verbose_name="师范生类别", max_length=128, null=True, blank=True)
    emp_direction = models.CharField(verbose_name="毕业去向", max_length=128, null=True, blank=True)
    emp_sign_type = models.CharField(verbose_name="报到证签发类别", max_length=128, null=True, blank=True)
    emp_sign_unit = models.CharField(verbose_name="报到证签往单位", max_length=128, null=True, blank=True)
    emp_sign_loc = models.CharField(verbose_name="签往单位所在地", max_length=128, null=True, blank=True)
    emp_file_unit = models.CharField(verbose_name="档案发往单位", max_length=128, null=True, blank=True)
    emp_file_phone = models.CharField(verbose_name="单位联系电话", max_length=128, null=True, blank=True)
    emp_file_loc = models.CharField(verbose_name="收档单位地址", max_length=128, null=True, blank=True)
    emp_file_postcode = models.CharField(verbose_name="收档单位邮政编码", max_length=128, null=True, blank=True)
    emp_info1 = models.CharField(verbose_name="备注", max_length=256, null=True, blank=True)
    emp_info2 = models.CharField(verbose_name="备注2", null=True, max_length=256, blank=True)
    emp_unit_code = models.CharField(verbose_name="单位组织机构代码", max_length=128, null=True, blank=True)
    emp_unit_deal = models.CharField(verbose_name="协议书", max_length=128, null=True, blank=True)
    emp_unit_name = models.CharField(verbose_name="单位名称", max_length=128, null=True, blank=True)
    emp_unit_hired = models.BooleanField(verbose_name="是否聘用", default=False)
    emp_unit_type = models.CharField(verbose_name="单位性质", max_length=128, null=True, blank=True)
    emp_unit_industry = models.CharField(verbose_name="单位行业", max_length=128, null=True, blank=True)
    emp_unit_loc = models.CharField(verbose_name="单位所在地", max_length=128, null=True, blank=True)
    emp_unit_jobtype = models.CharField(verbose_name="工作职位类别", max_length=128, null=True, blank=True)
    emp_unit_phone = models.CharField(verbose_name="单位联系电话", max_length=128, null=True, blank=True)
    emp_unit_communicate = models.CharField(verbose_name="单位联系人", max_length=128, null=True, blank=True)
    emp_stu_sendmethod = models.CharField(verbose_name="派出方式", max_length=128, null=True, blank=True)
    emp_stu_phone = models.CharField(verbose_name="毕业生手机号码", max_length=128, null=True, blank=True)
    emp_stu_qq = models.CharField(verbose_name="毕业生QQ", max_length=128, null=True, blank=True)
    emp_stu_email = models.CharField(verbose_name="毕业生电子邮箱", max_length=128, null=True, blank=True)
    emp_stu_homephone = models.CharField(verbose_name="家庭联系电话", max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = "就业信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.emp_stu.stu_name


# 姓名、学号、联系方式、家庭成员及联系方式、家庭成员工作单位、是否为建档立卡户、家庭主要情况。
class Poverty(models.Model):
    por_stu = models.OneToOneField(Student, on_delete=models.CASCADE, verbose_name="学生", null=True, blank=True,
                                   unique=True)
    por_id = models.CharField(verbose_name="学号", max_length=128, null=True, blank=True)
    por_tel = models.CharField(verbose_name="联系方式", max_length=128, null=True, blank=True)
    por_family1 = models.CharField(verbose_name="家庭成员1", max_length=128, null=True, blank=True)
    por_family1_tel = models.CharField(verbose_name="联系电话1", max_length=128, null=True, blank=True)
    por_family1_job = models.CharField(verbose_name="家庭成员1工作单位", max_length=128, null=True, blank=True)
    por_family2 = models.CharField(verbose_name="家庭成员2", max_length=128, null=True, blank=True)
    por_family2_tel = models.CharField(verbose_name="联系电话2", max_length=128, null=True, blank=True)
    por_family2_job = models.CharField(verbose_name="家庭成员2工作单位", max_length=128, null=True, blank=True)
    por_is_archived = models.BooleanField(verbose_name="是否为建档立卡户", default=False)
    por_info = models.TextField(verbose_name="家庭主要情况", null=True, blank=True)

    class Meta:
        verbose_name = "贫困生信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.por_stu.stu_name
