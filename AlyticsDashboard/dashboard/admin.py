from django.contrib import admin
from .models import *
from dashboard.models import Dashboard, Person, Course, Grade
from django.utils.safestring import mark_safe

# TODO:чтобы сделать меню Дэшборд(т.е график, созданный по функции) в панели админки,
#  надо написать модель для нее в файле /AlyticsDashboard/dashboard/models.py


# ------------------------------------
@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    list_display = ("function", "chart_preview", "interval", "pace", "prep_date")
    # readonly_fields = ("chart",)
    

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass
