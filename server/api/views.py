from django.shortcuts import render
from rest_framework import viewsets
from .models import Tasks
from .serializerr import   TodoItemSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TodoItemSerializer


