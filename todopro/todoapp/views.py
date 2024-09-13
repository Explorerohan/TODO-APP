from django.shortcuts import render,redirect
from .models import Todo
from django.utils.timezone import now
from django.utils import timezone
from datetime import timedelta,datetime
# Create your views here.
from datetime import datetime, timedelta

def add_todo(request):
    if request.method == 'POST':
        data = request.POST
        task = data.get('add-todo')
        date = data.get('due-date')
        time = data.get('due-time') 
        priorities = data.get('priority')
        
        Todo.objects.create(task=task, date=date,time=time, priorities=priorities, is_completed=False,completed_at=None)
        return redirect('/')


    tasks = Todo.objects.filter(is_completed=False)
    # Calculate the exact time left for each task
    for task in tasks:
        if task.date and task.time:
            due_datetime = datetime.combine(task.date, task.time)
            now = datetime.now()
            time_left = due_datetime - now
            
            if time_left < timedelta():
                task.time_left = "Overdue"
            else:
                days_left = time_left.days
                hours_left, remainder = divmod(time_left.seconds, 3600)
                minutes_left, seconds_left = divmod(remainder, 60)
                if days_left:
                    task.time_left = f"{days_left} days {hours_left} hours {minutes_left} minutes"
                elif hours_left:
                    task.time_left = f"{hours_left} hours {minutes_left} minutes"
                else:
                    task.time_left = f"{minutes_left} minutes"
        else:
            task.time_left = "Incomplete date/time information"
    
    completed_tasks = Todo.objects.filter(is_completed=True)

    return render(request, 'index.html', {
        'tasks': tasks,
        'completed_tasks': completed_tasks
    })


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

def delete_task(request,id):
    task = Todo.objects.get(id=id)
    task.delete()
    return redirect('/')


def edit_task(request,id):
    update = Todo.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        update.task = data.get('add-todo')
        date = data.get('due-date')
        time = data.get('due-time')
        priorities = data.get('priority')
        if date:
            update.date = date
        if time:
            update.time = time
        if priorities:
            update.priorities = priorities
        update.save()
        return redirect('/')
    return render(request,'edit_task.html',{'task':update})

def completed_task(request,id):
    task = Todo.objects.get(id=id)
    task.is_completed = True
    task.completed_at = timezone.now()
    task.save()
    return redirect('/')
    