from hashlib import sha256
from base64 import b32encode
from qrcode import QRCode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image, ImageDraw, ImageFont

from django.db.models import Sum
from django.utils.timezone import now, timedelta
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import (PlayerForm, AddPurchaseForm, AddAchieveForm, )
from .models import Player, Achieve


def index(request):
    context = {
        'page_obj': Player.objects.all()
    }
    return render(request, 'players.html', context)


def add_player(request):
    form = PlayerForm(request.POST or None)
    print(request.method, form.errors)
    if request.method == 'POST' and form.is_valid():
        player = form.save(commit=False)
        print(player)
        player.personal_hash = (
            b32encode(sha256(
                'Club'.encode('utf-8')
            ).digest()).decode().strip('=') + '-' +
            b32encode(sha256(
                (player.email+player.nick+player.telegram).lower(
                ).encode('utf-8')
            ).digest()).decode().strip('=')
        )
        player.save()
        player.personal_id = f'AK-{str(1+player.pk*111).rjust(7, "0")}'
        player.save()
        return redirect('players:player', player_id=player.pk)
    context = {'form': form}
    return render(request, 'edit_profile.html', context)


def player(request, player_id):
    form_purchase = AddPurchaseForm(request.POST or None)
    form_achive = AddAchieveForm(request.POST or None)
    player = Player.objects.get(pk=player_id)
    context = {
        'player': Player.objects.get(pk=player_id),
        'form_purchase': form_purchase,
        'form_achive': form_achive,
        'referer': request.headers['Referer']
    }
    # context = context | player.purchases.aggregate(Sum('total_price'))
    return render(request, 'player_profile.html', context)


def player_edit(request, player_id):
    player = Player.objects.get(pk=player_id)
    form = PlayerForm(request.POST or None, instance=player)
    print(player)
    if request.method == 'POST' and form.is_valid():
        player = form.save(commit=False)
        player.pk = player_id
        player.personal_id = f'AK-{str(1+player.pk*111).rjust(7, "0")}'
        player.personal_hash = (
            b32encode(sha256(
                'Club'.encode('utf-8')
            ).digest()).decode().strip('=') + '-' +
            b32encode(sha256(
                (player.email+player.nick+player.telegram).lower(
                ).encode('utf-8')
            ).digest()).decode().strip('=')
        )
        player.save()
        return redirect('players:player', player_id=player.pk)
    context = {"form": form, "is_edit": True}
    return render(request, "edit_profile.html", context)


def add_purchase(request, player_id):
    player = Player.objects.get(pk=player_id)
    form = AddPurchaseForm(request.POST or None)
    if form.is_valid():
        player.purchases.create(total_price=form.cleaned_data['purchase_sum'])
        player.save()
    return redirect('players:player', player_id=player_id)


def get_qr(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    qr = QRCode(version=1, border=5, box_size=10,
                error_correction=ERROR_CORRECT_H)
    qr.add_data(player.personal_hash)
    qrcode_img = qr.make_image(fill_color='white', back_color='black')
    chevron_img = ImageDraw.Draw(qrcode_img)
    font = ImageFont.truetype('static/FreeSans.ttf', size=32, encoding='UTF=8')
    chevron_img.text((qr.border*qr.box_size, qr.border*qr.box_size//2),
                     player.nick, align='center', font=font, anchor='lm',
                     fill='white')
    response = HttpResponse(content_type='image/png')
    logo_img = Image.open('static/img/club_logo_demo.png').resize((200, 200))
    qr_center = ((qrcode_img.size[0]-logo_img.size[0])//2,
                 (qrcode_img.size[1]-logo_img.size[1])//2)
    qrcode_img.paste(logo_img, qr_center, mask=logo_img)
    qrcode_img.save(response, 'PNG')
    return response


def add_achive(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    Achieve.objects.create(owner=player, valid_time=now()+timedelta(days=183))
    return redirect('players:player', player_id=player.pk)
