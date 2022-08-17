from django.contrib import admin
from .models import DifficultyTask, Task

# Register your models here.

class DifficultyTaskAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']
	list_display_links = ['id', 'name']

class TaskAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'created', 'modified']
	list_display_links = ['id', 'name']

admin.site.register(DifficultyTask, DifficultyTaskAdmin)
admin.site.register(Task, TaskAdmin)