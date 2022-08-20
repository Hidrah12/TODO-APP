from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['name', 'summary']

class TaskFormUpdate(forms.Form):
	name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'id': 'input_name', 'placeholder':'Task name here...', 'name': 'name_update'}))
	summary = forms.CharField(widget=forms.Textarea(attrs={'id': 'text_summary', 'placeholder': 'Description', 'name': 'summary_update'}))