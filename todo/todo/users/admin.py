from django.core import mail
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from todo.users.models import User
from todo.users.tasks.analyzer import Analyzer
from todo.core.decorators import message_user


class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'full_name', 'modified']
    list_filter = ['is_staff', 'tags']
    search_fields = ['email', 'full_name']
    readonly_fields = ['created', 'modified']
    fieldsets = [
        (None, {'fields': ['email', 'password']}),
        ('Details', {'fields': ['full_name', 'date_of_birth', 'tags']}),
        ('Permissions', {'fields': ['is_active', 'is_staff', 'is_superuser']}),
        ('System', {'classes': ['collapse'], 'fields': ['created', 'modified']}),
    ]
    add_fieldsets = [
        (None, {
            'classes': ['wide'],
            'fields': ['email', 'password1', 'password2']}
         ),
    ]
    ordering = ['-modified']
    filter_horizontal = []
    show_full_result_count = False
    actions = ['relaunch', 'notify_user']

    @message_user("Relaunched selected analyzers")
    def relaunch(self, request, queryset):
        for user in queryset:
            Analyzer().delay(user.id)
    relaunch.short_description = 'Relaunch analyzers'

    @message_user("Notified user")
    def notify_user(self, request, queryset):
        for user in queryset:
            mail.send_mail("Test subject", "Test email", settings.DEFAULT_FROM_EMAIL, [user.email])
    notify_user.short_description = 'Notify user'


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
