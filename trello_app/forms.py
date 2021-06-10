from django import forms
from trello_app.models import Task, TaskList, Board

class TaskListForm(forms.ModelForm):
  class Meta:
    model = TaskList
    # TODO: Add the 'board' field here
    fields = ['name']

class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['name', 'desc', 'due_date', 'list']
    widgets = {
      'due_date': forms.DateTimeInput(attrs= {'type': 'datetime-local'})
    }

class BoardForm(forms.ModelForm):
  # TODO: Add the meta class inside to show the board name field in the form
  # Created at field should not be shown in the form


  # Remove the next pass statement after done
  pass