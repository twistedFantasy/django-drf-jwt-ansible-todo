from todo.users.models import User

from django_filters.rest_framework import FilterSet, BooleanFilter, CharFilter
from rest_framework.filters import BaseFilterBackend


class UserFilter(FilterSet):
    name = CharFilter(field_name='full_name', lookup_expr='icontains')
    is_staff = BooleanFilter(field_name='is_staff')

    class Meta:
        model = User
        fields = ['email', 'name', 'full_name', 'date_of_birth', 'is_active', 'is_staff']


class UserBornAfterFilterBackend(BaseFilterBackend):
    """
        Custom Generic Filter which allow to show only users who were born after selected date.
        https://www.django-rest-framework.org/api-guide/filtering/#custom-generic-filtering
    """
    def filter_queryset(self, request, queryset, view):
        born_after = request.query_params.get('born_after')
        if born_after:
            queryset = queryset.filter(date_of_birth__gte=born_after)
        return queryset
