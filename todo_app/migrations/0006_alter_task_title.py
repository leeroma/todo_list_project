# Generated by Django 4.2.13 on 2024-05-07 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0005_alter_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Название'),
        ),
    ]
