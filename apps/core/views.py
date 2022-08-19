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
	if user:
		if request.method == 'POST':
			task_form = TaskForm(request.POST)
			if task_form.is_valid():
				task = Task.objects.create(
					name = task_form.cleaned_data['name'],
					summary = task_form.cleaned_data['summary'],
					important = request.POST['important'],
					user_id = request.session['user']['id']
				)
				task_form = TaskForm()
				tasks = Task.objects.filter(user_id = request.session['user']['id'])
				context_data = {
					'task_form': task_form,
					'tasks': tasks
				}
				return render(request, 'index.html', context_data)
			else:
				task_form = TaskForm(request.POST)
				tasks = Task.objects.filter(user_id = request.session['user']['id'])
				context_data = {
					'task_form': task_form,
					'tasks': tasks
				}
				return render(request, 'index.html', context_data)
			
	task_form = TaskForm()
	tasks = Task.objects.filter(user_id = request.session['user']['id']).order_by('-id')
	tasks_important = Task.objects.filter(important = 'true')
	context_data = {
		'task_form': task_form,
		'tasks': tasks,
		'tasks_important': tasks_important
	}
	return render(request, 'index.html', context_data)
