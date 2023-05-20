from django.db import models

from common.models import TimestampedModel


class Game(TimestampedModel):
    name = models.CharField('Название игры', max_length=50)
    date = models.DateField('Дата проведения')
    org = models.CharField('Ответственный судья', max_length=30)

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ('date',)

    def __str__(self) -> str:
        return f'{self.name} at {self.date}'
