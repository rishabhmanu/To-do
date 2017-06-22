from django.db import models

class Todo(models.Model):
    author = models.ForeignKey('auth.User')
    task = models.CharField(max_length=50)
    status = models.BooleanField()
    def publish(self):
        self.save()
    def __str__(self):
        return self.task
