from django.shortcuts import render,redirect
from .models import Todo
# Create your views here.
def add_todo(request):
    if request.method == 'POST':
        data = request.POST
        task = data.get('add-todo')
        date = data.get('due-date')
        priorities = data.get('priority')
        Todo.objects.create(task=task, date = date, priorities=priorities)
        return redirect('/')
    queryset = Todo.objects.all()
    context = {'tasks': queryset}
    return render(request, 'index.html',context)