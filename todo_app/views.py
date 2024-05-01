from django.shortcuts import render

from todo_app.models import Task


def home_page(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

