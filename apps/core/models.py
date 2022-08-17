from django.db import models

# Create your models here.

class DifficultyTask(models.Model):
	name = models.CharField(max_length=15)

	def __str__(self) -> str:
		return f'{self.name}'

class Task(models.Model):
	name = models.CharField(max_length=50)
	difficulty = models.ForeignKey(DifficultyTask, on_delete=models.PROTECT)
	summary = models.TextField(blank=True, null=True)
	id_user = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self) -> str:
		return f'{self.name}'