from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    task = models.CharField( max_length=50)
    date = models.DateTimeField()
    time = models.TimeField(default=timezone.now)
    priorities = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)