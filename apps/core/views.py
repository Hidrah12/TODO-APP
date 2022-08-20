from django.shortcuts import render, redirect
from .form import TaskForm, TaskFormUpdate
from .models import Task
from uuid import uuid1

def checkImportant(req, update):
	important = ''
	try:
		if update == True:
			important = req.POST['important_update']	
		else: 
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
					important = checkImportant(request, False),
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
	task_form_update = TaskFormUpdate()
	context_data = {
		'task_form': task_form,
		'task_form_update': task_form_update,
		'tasks': tasks
	}
	return render(request, 'index.html', context_data)

def delete_task(request, id):
	if request.method == 'POST':
		task = Task.objects.filter(id = id).first()
		if task:
			task.delete()
	return redirect('/')

def update_task(request, id):
	if request.method == 'POST':
		task_form_update = TaskFormUpdate(request.POST)
		if task_form_update.is_valid():
			task = Task.objects.get(id = id)
			print(task_form_update.cleaned_data)
			task.name = task_form_update.cleaned_data['name']
			task.summary = task_form_update.cleaned_data['summary']
			task.important = checkImportant(request, True)
			task.save()
	return redirect('/')

