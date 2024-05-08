from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from todo_app.forms import TaskForm
from todo_app.models import Task, STATUS_CHOICES


def home_page(request):
    tasks = Task.objects.all()
    if not tasks:
        return redirect('create_task')
    return render(request, 'index.html', {'tasks': tasks})


def create_task(request):
    form = TaskForm()
    statuses = STATUS_CHOICES
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return HttpResponseRedirect(reverse('task', args=[task.pk]))

    return render(request, 'create_task.html', context={'form': form, 'statuses': statuses})


def task(request, pk: int):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', {'task': task})


def delete_task(request, pk: int):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')


def edit_task(request, pk: int):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(initial=task.__dict__)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                task.title = form.cleaned_data['title'] or task.title
                task.description = form.cleaned_data['description'] or task.description
                task.status = form.cleaned_data['status'] or task.status
                task.deadline = form.cleaned_data['deadline'] or task.deadline
                task.save()
            return HttpResponseRedirect(reverse('task', args=[task.pk]))

    return render(request, 'edit_task.html', context={'task': task, 'form': form})


def delete_tasks(request):
    pks = request.POST.keys()
    for pk in pks:
        if pk.isnumeric():
            task = get_object_or_404(Task, pk=int(pk))
            task.delete()

    return redirect('home')
