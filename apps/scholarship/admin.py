from django.contrib import admin
from .models import ScholarshipBasic,ScholarshipApply
# Register your models here.

class ApplyInline(admin.TabularInline):
    model = ScholarshipApply
    autocomplete_fields = ['app_stu']

@admin.register(ScholarshipBasic)
class ScholarshipBasicAdmin(admin.ModelAdmin):
    list_display = ['sch_title','sch_type','sch_is_available']
    list_filter = list_display
    list_editable = ['sch_is_available']
    search_fields = ['sch_title']
    inlines = [ApplyInline]


@admin.register(ScholarshipApply)
class ScholarshipApplyAdmin(admin.ModelAdmin):
    list_display = ['app_sch','app_stu','app_tutor_score','app_moral_score','app_course_score','app_academy_score','app_social_score','app_review_results','app_general_score']
    list_filter = list_display
    autocomplete_fields = ['app_sch','app_stu']
    readonly_fields = ['app_general_score']
