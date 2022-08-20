from django.urls import path
from .views import home_view, update_task_view, delete_task_view
from .api import task_api_view

urlpatterns = [
	path('', home_view, name='home'),
	path('update-task/<int:id>/', update_task_view, name='update-task'),
	path('delete-task/<int:id>/', delete_task_view, name='delete-task'),
	path('api/task/<int:id>/', task_api_view, name='task-api'),
]