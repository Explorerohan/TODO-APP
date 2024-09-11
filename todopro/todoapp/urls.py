from django.urls import path
from.views import add_todo

app_name = 'todo'
urlpatterns = [
    path('',add_todo,name='add_todo'),
]
