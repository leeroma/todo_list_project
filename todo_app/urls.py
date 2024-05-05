from django.urls import path

from todo_app.views import home_page, add_task, adding, task, delete_task, changing_status, set_new_status

urlpatterns = [
    path('', home_page, name='home'),
    path('adding', adding, name='adding'),
    path('add_task', add_task, name='add_task'),
    path('task/<int:pk>', task, name='task'),
    path('delete_task/<int:pk>', delete_task, name='delete_task'),
    path('changing_status/<int:pk>', changing_status, name='changing_status'),
    path('set_new_status/<int:pk>', set_new_status, name='set_new_status'),

]
