# Generated by Django 4.2 on 2023-04-24 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_alter_game_options_alter_registration_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Registration',
        ),
    ]
