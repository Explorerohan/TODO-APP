from django.shortcuts import render,redirect
from .models import Todo
from django.utils.timezone import now
from datetime import timedelta
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
    for task in queryset:
        task.time_left = calculate_time_left(task.date)
    return render(request, 'index.html',context)

def calculate_time_left(due_date):
    if due_date is None:
        return "No due date"

    now_time = now()
    time_diff = due_date - now_time

    if time_diff <= timedelta(seconds=0):
        return "Expired"

    days = time_diff.days
    hours, remainder = divmod(time_diff.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    return f"{days}d {hours}h {minutes}m"
