from django.urls import path

from todo_app.views import home_page, create_task, task, delete_task, edit_task

urlpatterns = [
    path('', home_page, name='home'),
    path('create_task', create_task, name='create_task'),
    path('task/<int:pk>', task, name='task'),
    path('delete_task/<int:pk>', delete_task, name='delete_task'),
    path('edit_task/<int:pk>', edit_task, name='edit_task'),

]
