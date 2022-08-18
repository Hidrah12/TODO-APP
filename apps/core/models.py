from django.db import models

# Create your models here.

class Task(models.Model):
	name = models.CharField(max_length=50)
	summary = models.TextField(blank=True, null=True)
	user_id = models.CharField(max_length=100, db_index=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self) -> str:
		return f'{self.name}'