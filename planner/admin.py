from django.contrib import admin
from .models import WeeklyPlanner, DailyPlanner

@admin.register(WeeklyPlanner)
class WeeklyPlannerAdmin(admin.ModelAdmin):
    list_display = ('task_title', 'is_priority', 'specific_time', 'type_of_task', 'status')
    list_filter = ('is_priority', 'type_of_task', 'status')
    search_fields = ('task_title', 'short_description')
    ordering = ('-is_priority', 'specific_time')

@admin.register(DailyPlanner)
class DailyPlannerAdmin(admin.ModelAdmin):
    list_display = ('task_title', 'is_priority', 'specific_time', 'type_of_type', 'status')
    list_filter = ('is_priority', 'type_of_type', 'status')
    search_fields = ('task_title',)
    ordering = ('-is_priority', 'specific_time')
