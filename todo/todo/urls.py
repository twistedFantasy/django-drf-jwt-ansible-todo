import debug_toolbar
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from todo.users.views import UserViewSet, ToDoTokenObtainPairView
from todo.tasks.views import TaskViewSet


admin.autodiscover()
suffix = '' if settings.ENV == 'prd' else ' %s' % settings.ENV.upper()
admin.site.site_header = settings.NAME + suffix
admin.site.site_title = settings.NAME + suffix

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    # built-in
    path('admin/', admin.site.urls),

    # 3rd party apps
    path('__debug__/', include(debug_toolbar.urls)),
    # path('health/', include('health_check.urls')),

    path('api/v1/token/obtain/', ToDoTokenObtainPairView.as_view(), name='auth'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='verify'),

    # our apps
    path('api/v1/', include(router.urls)),
]
