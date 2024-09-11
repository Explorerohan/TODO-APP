from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField( max_length=50)
    date = models.DateTimeField()
    priorities = models.CharField(max_length=50)