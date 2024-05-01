from django.urls import path

from todo_app.views import home_page, add_task, adding, task, delete_task

urlpatterns = [
    path('', home_page, name='home'),
    path('adding', adding, name='adding'),
    path('add_task', add_task, name='add_task'),
    path('task/<int:pk>', task, name='task'),
    path('delete_task/<int:pk>', delete_task, name='delete_task'),

]
