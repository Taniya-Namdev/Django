from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def home(request):
    # return HttpResponse("Hello World, You are at my BOOKSTORE")
     return render(request,'index.html')
         
     
def about(request):
    # return HttpResponse("Hello World, You are at my about page of BOOKSTORE")
    return render(request,'contact.html')
def contact(request):
    # return HttpResponse("Hello World, You are at my contact page of BOOKSTORE")
     return render(request,'about.html')
def task_list(request): 
    tasks = Task.objects.all() 
    return render(request, 'task_list.html', {'tasks': tasks}) 
def task_create(request): 
    if request.method == 'POST':
         form = TaskForm(request.POST) 
         if form.is_valid(): 
            form.save()
            return redirect('task_list') 
         else: 
            form = TaskForm() 
            return render(request, 'task_form.html', {'form': form})
    
def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('task_list')
def task_list(request):
    tasks = Task.objects.all().order_by('id')  # or any other ordering criteria
    return render(request, 'task_list.html', {'tasks': tasks})
