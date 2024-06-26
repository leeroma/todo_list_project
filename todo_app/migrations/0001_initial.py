# Generated by Django 5.0.4 on 2024-05-01 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=3000, verbose_name='Описание')),
                ('status', models.CharField(choices=[('new', 'Новое'), ('wip', 'В процессе'), ('done', 'Выполнено')], default=('new', 'Новое'), max_length=15, verbose_name='Описание')),
                ('deadline', models.DateField(blank=True, default='', verbose_name='Дата выполнения')),
            ],
        ),
    ]
