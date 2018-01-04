from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Task
from .forms import PostForm
from django.shortcuts import redirect
from rest_framework import viewsets
from .serializers import TaskSerializer

def task_list(request):
    tasks = Task.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    return render(request, 'todoapp/task_list.html', {'tasks':tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todoapp/task_detail.html', {'task': task})

def task_add(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)

            task.created_at = timezone.now()
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = PostForm()
    return render(request, 'todoapp/task_edit.html', {'form': form})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)

            task.created_at = timezone.now()
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = PostForm(instance=task)
    return render(request, 'todoapp/task_edit.html', {'form': form})


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    serializer_class = TaskSerializer