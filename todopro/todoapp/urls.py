from django.urls import path
from.views import add_todo,delete_task,edit_task

app_name = 'todo'
urlpatterns = [
    path('',add_todo,name='add_todo'),
    path('delete/<id>/',delete_task,name='delete_task'),
    path('edit/<id>/',edit_task,name='edit_task'),
]
