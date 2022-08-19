from django.shortcuts import render, redirect
from .form import TaskForm
from .models import Task
from uuid import uuid1

def checkImportant(req):
	important = ''
	try:
		important = req.POST['important']
	except:
		important = 'false'
	return important

def home_view(request):
	session = request.session
	user = session.get('user')
	if not user:
		user = session['user'] = {
			'id': uuid1().urn
		}
	if user:
		tasks = Task.objects.filter(user_id = request.session['user']['id']).order_by('-id')
		if request.method == 'POST':
			task_form = TaskForm(request.POST)
			if task_form.is_valid():
				Task.objects.create(
					name = task_form.cleaned_data['name'],
					summary = task_form.cleaned_data['summary'],
					important = checkImportant(request),
					user_id = request.session['user']['id']
				)
				task_form = TaskForm()
				context_data = {
					'task_form': task_form,
					'tasks': tasks
				}
				return redirect('/')
			else:
				task_form = TaskForm(request.POST)
				context_data = {
					'task_form': task_form,
					'tasks': tasks
				}
				return redirect('/')

	task_form = TaskForm()
	context_data = {
		'task_form': task_form,
		'tasks': tasks
	}
	return render(request, 'index.html', context_data)

def delete_task(request, id):
	if request.method == 'POST':
		task = Task.objects.filter(id = id).first()
		if task:
			task.delete()
	return redirect('/')