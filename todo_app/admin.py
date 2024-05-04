from django.contrib import admin

from todo_app.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )
    list_filter = ('status', )
    search_fields = ('title', 'description', )
    exclude = []


admin.site.register(Task, TaskAdmin)
