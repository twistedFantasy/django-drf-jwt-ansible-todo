from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from todo.tasks.models import Task
from todo.tasks.serializers import TaskSerializer
from todo.tasks.filters import UserFilterBackend
from todo.core.permissions import IsAllowedMethodOrStaff, IsObjectOwnerOrStaff


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsAllowedMethodOrStaff, IsObjectOwnerOrStaff]
    filter_backends = [OrderingFilter, UserFilterBackend, DjangoFilterBackend]
    filter_fields = ['user', 'type', 'is_completed']
