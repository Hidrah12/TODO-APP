from django.urls import path
from .views import delete_task, home_view, update_task
from .api import task_api_view

urlpatterns = [
	path('', home_view, name='home'),
	path('delete/<int:id>/', delete_task, name='delete-task'),
	path('update-task/<int:id>/', update_task, name='update-task'),
	path('api/task/<int:id>/', task_api_view, name='task-api-view'),
]