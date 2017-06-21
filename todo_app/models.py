from django.db import models
from django.utils import timezone

class Todo(models.Model):
    author = models.ForeignKey('auth.User')
    task = models.CharField(max_length=50)
    status = models.BooleanField()
    def __str__(self):
        return self.task
