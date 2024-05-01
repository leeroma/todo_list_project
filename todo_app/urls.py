from django.urls import path

from todo_app.views import home_page, add_task

urlpatterns = [
    path('', home_page, name='home'),
    path('add_task', add_task, name='add_task'),

]
