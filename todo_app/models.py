from django.db import models


STATUS_CHOICES = (
    ('new', 'Новое'),
    ('wip', 'В процессе'),
    ('done', 'Выполнено'),
)


class Task(models.Model):
    title = models.CharField('Название', default='Без названия', max_length=300, null=False, blank=False)
    description = models.TextField('Описание', max_length=3000, null=False, blank=False)
    status = models.CharField('Статус', choices=STATUS_CHOICES, default='new', max_length=15, null=False)
    deadline = models.DateField('Дата выполнения', blank=True, default=None, null=True)

    def __str__(self):
        return f'{self.title} - {self.status}'
