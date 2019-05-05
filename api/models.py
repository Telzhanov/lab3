from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class TaskList(models.Model):
    name = models.CharField(max_length=200)


class Task(models.Model):
    name = models.CharField('Name',max_length=200)
    created_at = models.DateTimeField('Created_at', auto_now_add=True)
    due_on = models.DateTimeField('Due_on', null=False)
    status = models.CharField('Status', max_length=200)
    task_list = models.ForeignKey(TaskList, related_name='tasks', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE, default=None, null=True)

