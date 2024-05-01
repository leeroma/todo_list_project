from django.shortcuts import render, redirect

from todo_app.models import Task


def home_page(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def add_task(request):
    data = request.POST
    Task.objects.create(description=data['description'], deadline=data['deadline'])
    return redirect('home')
