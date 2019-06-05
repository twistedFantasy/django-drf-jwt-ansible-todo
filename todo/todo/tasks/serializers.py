from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework import serializers

from todo.tasks.models import Task


class TaskSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Task
        exclude = []
        read_only_fields = ['created', 'modified']

