# Generated by Django 5.0.4 on 2024-05-01 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_alter_task_deadline_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Дата выполнения'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('new', 'Новое'), ('wip', 'В процессе'), ('done', 'Выполнено')], default='new', max_length=15, verbose_name='Статус'),
        ),
    ]