from django.contrib import admin
from .models import Semester, Departure, Score
from .forms import DepartureForm


# Register your models here.


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ['sem_name', 'sem_is_available', 'sem_dep_status']
    search_fields = ['sem_name']
    list_editable = ['sem_is_available','sem_dep_status']


@admin.register(Departure)
class DepartureAdmin(admin.ModelAdmin):
    list_display = ['depart_semster', 'depart_type', 'depart_stu', 'get_class', 'depart_datetime', 'depart_loc', ]
    autocomplete_fields = ['depart_stu', 'depart_semster']
    list_filter = ['depart_semster', 'depart_type', 'depart_stu', 'depart_datetime', 'depart_loc',
                   'depart_stu__stu_class__cls_name']


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ['sco_sem', 'sco_cls', 'sco_stu', 'sco_course', 'sco_score']
    list_filter = list_display
    autocomplete_fields = ['sco_cls', 'sco_sem', 'sco_stu']
