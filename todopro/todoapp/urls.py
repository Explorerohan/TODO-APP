from django.urls import path
from.views import add_todo,delete_task

app_name = 'todo'
urlpatterns = [
    path('',add_todo,name='add_todo'),
    path('delete/<id>/',delete_task,name='delete_task'),
]
