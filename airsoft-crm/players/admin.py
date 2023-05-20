from django.contrib import admin

from players.models import Player, Achieve, Registration, Purchase
from games.models import Game

admin.site.register(Player)
admin.site.register(Game)
admin.site.register(Registration)
admin.site.register((Achieve, Purchase,))
