from django.contrib import admin
from .models import Thesis, Patent, Prize, Scholarship, Honor,Fund


# Register your models here.

@admin.register(Thesis)
class ThesisAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Thesis._meta.get_fields()]
    # readonly_fields = ['ths_stu']
    list_filter = list_display
    autocomplete_fields=['ths_stu']


@admin.register(Patent)
class PatentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Patent._meta.get_fields()]
    # readonly_fields = ['pat_stu']
    list_filter = list_display
    autocomplete_fields=['pat_stu']


@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Scholarship._meta.get_fields()]
    # readonly_fields = ['sch_stu']
    list_filter = list_display
    autocomplete_fields=['sch_stu']


@admin.register(Prize)
class PrizeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Prize._meta.get_fields()]
    # readonly_fields = ['pri_stu']
    list_filter = list_display
    autocomplete_fields=['pri_stu']



@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Fund._meta.get_fields()]
    # readonly_fields = ['fund_stu']
    list_filter = list_display
    autocomplete_fields=['fund_stu']



@admin.register(Honor)
class HonorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Honor._meta.get_fields()]
    # readonly_fields = ['hon_stu']
    list_filter = list_display
    autocomplete_fields=['hon_stu']

