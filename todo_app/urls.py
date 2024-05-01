from django.urls import path

from todo_app.views import home_page


urlpatterns = [
    path('', home_page, name='home'),

]
