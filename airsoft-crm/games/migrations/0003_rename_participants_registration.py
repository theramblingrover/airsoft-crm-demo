# Generated by Django 4.2 on 2023-04-14 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0009_alter_player_personal_hash'),
        ('games', '0002_alter_game_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Participants',
            new_name='Registration',
        ),
    ]
