from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Task

@api_view(['GET', 'PUT'])
def task_api_view(request, id):
	if request.method == 'GET':
		task = Task.objects.filter(id=id).first()
		if task:
			task_serializer = TaskSerializer(task)
			return Response(task_serializer.data, status = status.HTTP_200_OK)
	elif request.method == 'PUT':
		print(request.body)
		return Response(status = status.HTTP_200_OK)
	else:
		return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)