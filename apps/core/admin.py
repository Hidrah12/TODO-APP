from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'created', 'modified']
	list_display_links = ['id', 'name']

admin.site.register(Task, TaskAdmin)