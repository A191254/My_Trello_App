from django.db import models
from django.utils import timezone

# Create your models here.
class Board(models.Model):
  # TODO: Add name field with max_length = 50
  
  # TODO: Add created_at field with default value as timezone.now()
  
  # Remove the next line pass when done with above
  pass

class TaskList(models.Model):
  name = models.CharField(max_length=50)
  created_at = models.DateTimeField(
    default=timezone.now()
  )
  # TODO: Add board field which is foreign key to the Board model
  # board = ...

  def __str__(self):
    return f"{self.name}"

class Task(models.Model):
  name = models.CharField(max_length=50)
  desc = models.TextField()
  created_at = models.DateTimeField(
    default=timezone.now()
  )
  due_date = models.DateTimeField()
  list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.name}"