from django.contrib import admin
from .models import Student, Employment, Poverty
from .utils import fieldsets
from award.models import Thesis, Patent, Scholarship, Prize, Fund, Honor


class StudentInline(admin.StackedInline):
    model = Student
    fields = ("stu_id", "stu_name")
    extra = 0
    # 显示跳转超链接
    show_change_link = True


class EmployInline(admin.StackedInline):
    model = Employment
    extra = 0
    show_change_link = True
    classes = ['collapse']
    fieldsets = fieldsets.EmploymentInlineFieldSets


class PovertyInline(admin.StackedInline):
    model = Poverty
    extra = 0
    show_change_link = True
    classes = ['collapse']
    fieldsets = fieldsets.PovertyInlineFieldSets


class ThesisInline(admin.TabularInline):
    classes = ['collapse']
    model = Thesis
    extra = 1
    show_change_link = True


class PatentInline(admin.TabularInline):
    classes = ['collapse']
    model = Patent
    extra = 1
    show_change_link = True


class ScholarshipInline(admin.TabularInline):
    classes = ['collapse']
    model = Scholarship
    extra = 1
    show_change_link = True


class PrizeInline(admin.TabularInline):
    classes = ['collapse']
    model = Prize
    extra = 1
    show_change_link = True


class FundInline(admin.TabularInline):
    classes = ['collapse']
    model = Fund
    extra = 1
    show_change_link = True


class HonorInline(admin.TabularInline):
    classes = ['collapse']
    model = Honor
    extra = 1
    show_change_link = True
