from rest_framework.serializers import ModelSerializer
from drf_dynamic_fields import DynamicFieldsMixin

from todo.users.models import User
from todo.tasks.serializers import TaskSerializer
from todo.core.serializers import CustomTokenObtainPairSerializer


class TodoTokenObtainPairSerializer(CustomTokenObtainPairSerializer):
    pass


class StaffUserSerializer(DynamicFieldsMixin, ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'is_staff']


class UserSerializer(StaffUserSerializer):

    class Meta(StaffUserSerializer.Meta):
        read_only_fields = ['email', 'is_staff']


class StaffUserWithTasksSerializer(StaffUserSerializer):
    tasks = TaskSerializer(many=True, required=False)

    class Meta(StaffUserSerializer.Meta):
        fields = StaffUserSerializer.Meta.fields + ['tasks']


class UserWithTasksSerializer(UserSerializer):
    tasks = TaskSerializer(many=True, required=False, read_only=True)

    class Meta(UserSerializer.Meta):
        fields = StaffUserSerializer.Meta.fields + ['tasks']
        read_only_fields = UserSerializer.Meta.read_only_fields + ['tasks']
