from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Task
from .forms import TaskForm
from django.db.models import Sum

def index(request):
  tasks = Task.objects.all()
  total_time = tasks.aggregate(Sum('time'))
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      new_task = form.save()
      return HttpResponseRedirect('/')
  else:
    form = TaskForm()
  return render(request, 'index.html', {'form':form, 'tasks':tasks, 'total_time': total_time })

def delete_task(request, task_id):
  Task.objects.get(pk=task_id).delete()
  return redirect('index')





