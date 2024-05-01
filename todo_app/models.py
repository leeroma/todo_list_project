from django.db import models


STATUS_CHOICES = (
    ('new', 'Новое'),
    ('wip', 'В процессе'),
    ('done', 'Выполнено'),
)


class Task(models.Model):
    description = models.TextField('Описание', max_length=3000, null=False, blank=False)
    status = models.CharField('Описание', choices=STATUS_CHOICES, default=STATUS_CHOICES[0], max_length=15, null=False)
    deadline = models.DateField('Дата выполнения', blank=True, default='')

    def __str__(self):
        return f'{self.description} - {self.status}'
