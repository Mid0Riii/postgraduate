from django.contrib import admin
from .models import Thesis, Patent, Prize, Scholarship, Honor, Fund


@admin.register(Thesis)
class ThesisAdmin(admin.ModelAdmin):
    """
    论文Admin视图
    """
    list_display = [field.name for field in Thesis._meta.get_fields()]
    # readonly_fields = ['ths_stu']
    list_filter = list_display
    autocomplete_fields = ['ths_stu']


@admin.register(Patent)
class PatentAdmin(admin.ModelAdmin):
    """
    专利Admin视图
    """
    list_display = [field.name for field in Patent._meta.get_fields()]
    # readonly_fields = ['pat_stu']
    list_filter = list_display
    autocomplete_fields = ['pat_stu']


@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
    """
    奖学金Admin视图
    """
    list_display = [field.name for field in Scholarship._meta.get_fields()]
    # readonly_fields = ['sch_stu']
    list_filter = list_display
    autocomplete_fields = ['sch_stu']


@admin.register(Prize)
class PrizeAdmin(admin.ModelAdmin):
    """
    获奖情况Admin视图
    """
    list_display = [field.name for field in Prize._meta.get_fields()]
    # readonly_fields = ['pri_stu']
    list_filter = list_display
    autocomplete_fields = ['pri_stu']


@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
    """
    专项资金Admin视图
    """
    list_display = [field.name for field in Fund._meta.get_fields()]
    # readonly_fields = ['fund_stu']
    list_filter = list_display
    autocomplete_fields = ['fund_stu']


@admin.register(Honor)
class HonorAdmin(admin.ModelAdmin):
    """
    荣誉称号Admin视图
    """
    list_display = [field.name for field in Honor._meta.get_fields()]
    # readonly_fields = ['hon_stu']
    list_filter = list_display
    autocomplete_fields = ['hon_stu']
