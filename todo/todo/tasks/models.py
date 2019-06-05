from django.db import models
from model_utils.choices import Choices

from todo.users.models import User
from todo.core.models import BaseModel


TYPE = Choices(('home', 'Home'), ('office', 'Office'), ('other', 'Other'))


class Task(BaseModel):
    user = models.ForeignKey(User, related_name='tasks', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=64)
    description = models.TextField('Description', null=True, blank=True)
    type = models.CharField('Type', max_length=32, default=TYPE.other, choices=TYPE, db_index=True)
    is_completed = models.BooleanField('Is Completed', default=False)
    start_date = models.DateField('Start Date', null=True, blank=True)
    end_date = models.DateField('End Date', null=True, blank=True)
    analyzer_date = models.DateField('Analyzer Date', null=True, blank=True)

    def __str__(self):
        return f'{self.name} (task {self.id})'

    class Meta:
        app_label = 'tasks'
        verbose_name_plural = 'Tasks'
        ordering = ['name']
