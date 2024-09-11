from django.shortcuts import render,redirect
from .models import Todo
from django.utils.timezone import now
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
        
        Todo.objects.create(task=task, date=date,time=time, priorities=priorities)
        return redirect('/')

    queryset = Todo.objects.all()
    context = {'tasks': queryset}

    # Calculate the exact time left for each task
    for task in queryset:
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

    return render(request, 'index.html', context)


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
