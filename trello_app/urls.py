from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('new_board', views.add_board, name='create_board'),
  path('board/<int:id>', views.show_board, name='display_board'),
  path('new_task/<int:list_id>', views.add_task_form, name='create_task'),
  path('new_list/<int:board_id>', views.add_task_list_form, name='create_list'),
  path('list/<int:id>', views.show_list, name='display_list'),
]