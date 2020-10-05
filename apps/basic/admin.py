from django.contrib import admin
from .models import StudentClass, Student, Tutor, Employment, Poverty
from .utils import fieldsets
from .inlines import *


# class StudentInline(admin.StackedInline):
#     model = Student
#     fields = ("stu_id", "stu_name")
#     extra = 0
#     # 显示跳转超链接
#     show_change_link = True
#
#
# class EmployInline(admin.StackedInline):
#     model = Employment
#     extra = 0
#     show_change_link = True
#     classes = ['collapse']
#     fieldsets = fieldsets.EmploymentInlineFieldSets
#
#
# class PovertyInline(admin.StackedInline):
#     model = Poverty
#     extra = 0
#     show_change_link = True
#     classes = ['collapse']
#     fieldsets = fieldsets.PovertyInlineFieldSets


@admin.register(StudentClass)
class ClassAdmin(admin.ModelAdmin):
    search_fields = ['cls_name']
    inlines = [StudentInline]
    list_display = ['cls_name']
    list_filter = ['cls_name']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    actions = ["send_message"]
    search_fields = ['stu_id','stu_name']
    list_display = ['stu_id', 'stu_name', 'stu_college', 'stu_class', "stu_tutor", 'stu_major', 'stu_gender', 'stu_tel',
                    'stu_birth']
    list_filter = list_display
    fieldsets = fieldsets.StudentFieldSets
    # 修改外键样式为异步搜索,需要配置外键所在模型searchfield
    autocomplete_fields = ['stu_tutor','stu_class','stu_usr']

    def get_form(self, request, obj=None, **args):
        """
        重写表单方法，当obj=None时，即为新建界面，此时不显示内连的就业信息和贫困生信息
        屏蔽掉外键冲突的问题
        """
        defaults = {}
        if obj is not None:
            self.inlines = [EmployInline, PovertyInline, ThesisInline, PatentInline, ScholarshipInline, PrizeInline,
                            FundInline, HonorInline]
        else:
            self.inlines = []
        defaults.update(args)
        return super(StudentAdmin, self).get_form(request, obj, **defaults)

    def send_message(self, request, queryset):
        print(queryset)

    send_message.short_description = "发送信息"
    send_message.icon = "fas fa-envelope"
    send_message.type = "info"


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ["tut_name", "tut_communication", "tut_dorm", "tut_loc", "tut_fam", "tut_fam_tel"]
    search_fields = ["tut_name"]


@admin.register(Employment)
class EmployAdmin(admin.ModelAdmin):
    # inlines = [StudentInline,]
    list_display = [field.name for field in Employment._meta.get_fields() if field.name != "id"]
    readonly_fields = ['emp_stu', 'emp_id', 'emp_gender', 'emp_loc']
    list_filter = ["emp_id", "emp_stu", "emp_gender", "emp_loc"]
    fieldsets = fieldsets.EmploymentFieldSets
    autocomplete_fields = ['emp_stu']


@admin.register(Poverty)
class PovertyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Poverty._meta.get_fields() if field.name != "id"]
    readonly_fields = ['por_stu', 'por_id', ]
    list_filter = ["por_stu", "por_id", "por_is_archived"]
    fieldsets = fieldsets.PovertyFieldSets
    autocomplete_fields = ['por_stu']



admin.site.site_header = '研究生管理系统'
admin.site.site_title = "研究生管理系统"
