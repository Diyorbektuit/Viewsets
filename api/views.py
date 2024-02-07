from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializers


class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers

