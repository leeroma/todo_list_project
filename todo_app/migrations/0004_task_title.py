# Generated by Django 5.0.4 on 2024-05-04 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_alter_task_deadline_alter_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default='Без названия', max_length=300, verbose_name='Название'),
        ),
    ]
