from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *
from rest_framework.filters import SearchFilter, OrderingFilter
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = TaskFilter
    search_fields = ['title']
    ordering_fields = ['created']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Create your views here.
