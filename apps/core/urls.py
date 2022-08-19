from django.urls import path
from .views import delete_task, home_view

urlpatterns = [
	path('', home_view, name='home'),
	path('delete/<int:id>/', delete_task, name='delete-task'),
]