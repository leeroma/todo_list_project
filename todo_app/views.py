from django.shortcuts import render, redirect, get_object_or_404

from todo_app.models import Task, STATUS_CHOICES


def home_page(request):
    tasks = Task.objects.all()
    if not tasks:
        return redirect('adding')
    return render(request, 'index.html', {'tasks': tasks})


def adding(request):
    statuses = STATUS_CHOICES
    return render(request, 'add_task.html', {'statuses': statuses})


def add_task(request):
    data = request.POST
    if data['deadline']:
        Task.objects.create(description=data['description'], status=data['status'], deadline=data['deadline'])
    else:
        Task.objects.create(description=data['description'], status=data['status'])

    return redirect('home')


def task(request, pk: int):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', {'task': task})


def delete_task(request, pk: int):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')
