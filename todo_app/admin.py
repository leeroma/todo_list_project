from django.contrib import admin

from todo_app.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', )
    list_filter = ('status', )
    search_fields = ('description', )
    exclude = []


admin.site.register(Task, TaskAdmin)
