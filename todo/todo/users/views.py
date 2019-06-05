from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from todo.users.models import User
from todo.users.permissions import IsCurrentUserOrStaff, CustomIsAllowedMethodOrStaff
from todo.users.filters import UserFilter, UserBornAfterFilterBackend
from todo.users.serializers import StaffUserSerializer, UserSerializer, StaffUserWithTasksSerializer, \
    UserWithTasksSerializer, TodoTokenObtainPairSerializer
from todo.core.filters import ObjectFieldFilterBackend
from todo.core.views import CustomTokenObtainPairView
from todo.core.helpers import true


class ToDoTokenObtainPairView(CustomTokenObtainPairView):
    user = User
    serializer_class = TodoTokenObtainPairSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, CustomIsAllowedMethodOrStaff, IsCurrentUserOrStaff]
    filter_backends = [
        ObjectFieldFilterBackend, SearchFilter, OrderingFilter, UserBornAfterFilterBackend, DjangoFilterBackend
    ]
    filterset_class = UserFilter
    search_fields = ['email', 'full_name']
    ordering_fields = ['email', 'full_name']
    ordering = ['email']

    def get_serializer_class(self):
        if true(self.request.query_params.get('tasks')):
            return StaffUserWithTasksSerializer if self.request.user.is_staff else UserWithTasksSerializer
        return StaffUserSerializer if self.request.user.is_staff else UserSerializer
