from django.db import models

from common.models import TimestampedModel
from games.models import Game


class Player(TimestampedModel):
    nick = models.CharField('Позывной', max_length=30)
    email = models.EmailField('E-mail', unique=True)
    telegram = models.CharField('Telegram', max_length=50)
    personal_id = models.CharField('Персональный номер', max_length=10,
                                   unique=True, blank=True, null=True)
    personal_hash = models.CharField('Машиночитаемый ID', max_length=500,
                                     unique=True, db_index=True)
    birthday = models.DateField('Дата рождения', auto_now_add=False,
                                auto_now=False, null=True, blank=True)

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'

    def __str__(self) -> str:
        return self.nick

    @property
    def purchase_sum(self):
        return self.purchases.aggregate(
            models.Sum('total_price'))['total_price__sum'] or 0


class Achieve(TimestampedModel):
    owner = models.ForeignKey(Player, on_delete=models.CASCADE,
                              related_name='achieves', null=True)
    valid_time = models.DateField(null=True)

    class Meta:
        ordering = ('valid_time',)
        get_latest_by = ('-valid_time',)

    def __str__(self):
        return f'Valid: {self.valid_time} for {self.owner}'


class Registration(TimestampedModel):
    game = models.ForeignKey(Game, on_delete=models.RESTRICT,
                             related_name='participants')
    player = models.ForeignKey(Player, on_delete=models.RESTRICT,
                               related_name='games')
    player_hash = models.CharField('QR или NFC', max_length=300)

    class Meta:
        verbose_name = 'Регистрация'
        verbose_name_plural = 'Регистрации'

    def __str__(self) -> str:
        return f'{self.player.nick} зарегистрирован на {self.game}'


class Purchase(TimestampedModel):
    owner = models.ForeignKey(Player, on_delete=models.RESTRICT,
                              related_name='purchases')
    total_price = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Покупка в магазине'
        verbose_name_plural = 'Покупка в магазине'
