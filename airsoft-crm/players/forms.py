from django.forms import (ModelForm, IntegerField, BooleanField, Form,
                          HiddenInput)

from .models import Player, Registration


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ["nick", "email", 'telegram', 'birthday', 'personal_id']


class AddPurchaseForm(Form):
    purchase_sum = IntegerField(label='Новая покупка', min_value=1,
                                help_text='Сумма покупки')


class AddAchieveForm(Form):
    pass


class GameRegisterForm(ModelForm):
    class Meta:
        model = Registration
        fields = ('player_hash',)


class GameConfirmForm(Form):
    player_id = IntegerField(widget=HiddenInput)
    game_id = IntegerField(widget=HiddenInput)
    achieve = BooleanField(required=False, label='Списать бесплатную игру')
