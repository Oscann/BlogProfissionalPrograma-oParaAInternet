from django.contrib import admin
from .models import Courses, Skill, Project, Technology

# Register your models here.
@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display=['name', 'coordination']
    search_fields=['name']
    list_filter=['coordination']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display=['name', 'expertise']
    search_fields=['name']

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display=['name']
    search_fields=['name']

@admin.register(Project)
class ProjectAdmini(admin.ModelAdmin):
    list_display=['name', 'coordination']
    search_fields=['name', 'coordination']
    list_filter=['coordination']