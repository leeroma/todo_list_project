from django import forms

from todo_app.models import Task


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.ModelForm):

    deadline = forms.DateField(widget=DateInput(format='%Y-%m-%d'), required=False, label='Дата выполнения')

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'deadline', ]

