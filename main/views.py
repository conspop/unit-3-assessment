from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Task
from .forms import TaskForm

def index(request):
  tasks = Task.objects.all()
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      new_task = form.save()
      return HttpResponseRedirect('/')
  else:
    form = TaskForm()
  return render(request, 'index.html', {'form':form, 'tasks':tasks })

def delete_task(request, task_id):
  Task.objects.get(pk=task_id).delete()
  return redirect('index')





