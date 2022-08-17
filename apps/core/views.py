from django.shortcuts import render
from .models import Task
from uuid import uuid1
from .form import TaskForm
from django.urls import reverse

def home_view(request):
	session = request.session
	user = session.get('user')
	if not user:
		user = session['user'] = {
			'id': uuid1().urn
		}
	else:
		if request.method == 'POST':
			task_form = TaskForm(request.POST)
			if task_form.is_valid():
				new_task = Task.objects.create(
					name = task_form.cleaned_data['name'],
					difficulty = task_form.cleaned_data['difficulty'],
					summary = task_form.cleaned_data['summary'],
					user_id = request.session['user']['id']
				)
				return reverse('home')
			else:
				task_form = TaskForm(request.POST)
				return render(request, 'index.html', {'task_form': task_form})
		else:
			task_form = TaskForm()
			tasks_user = Task.objects.filter(user_id = request.session['user']['id'])
			context_data = {
				'task_form': task_form,
				'tasks_user': tasks_user
			}
	return render(request, 'index.html', context_data)
