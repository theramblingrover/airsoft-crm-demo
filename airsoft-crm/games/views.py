from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now

from .models import Game
from players.models import Player, Registration
from players.forms import GameRegisterForm, GameConfirmForm


def index(request):
    context = {
        'page_obj': Game.objects.filter(date__gte=now())
    }
    return render(request, 'games.html', context)


def game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    form = GameRegisterForm(request.POST or None)
    context = {
        'game': game,
        'registrations': game.participants.all(),
        'form': form,
    }
    return render(request, 'game.html', context)


def confirm_registration(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    form = GameRegisterForm(request.POST or None)
    player_hash = form.data['player_hash']
    player = get_object_or_404(Player, personal_hash=player_hash)
    confirm_form = GameConfirmForm({
        'player_id': player.pk,
        'game_id': game.pk},
        use_required_attribute=False)
    context = {
        'player': player,
        'game': game,
        'form': confirm_form
    }
    if player.achieves.filter(valid_time__gte=now()):
        player.achieves.filter(valid_time__lt=now()).delete()
        context['achieve'] = player.achieves.latest()
    return render(request, 'reg_confirm.html', context)


def game_registration(request, game_id):
    form = GameConfirmForm(request.POST or None)
    game = get_object_or_404(Game, pk=game_id)
    player = get_object_or_404(Player, pk=form.data['player_id'])
    if not Registration.objects.filter(player=player,  game=game).exists():
        if form.data.get('achieve', False):
            player.achieves.latest().delete()
        Registration.objects.create(player=player, game=game)
    return redirect('games:game', game_id=game.pk)
