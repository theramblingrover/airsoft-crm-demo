# Generated by Django 4.2 on 2023-04-11 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_alter_player_options_player_personal_hash_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='Персональный номер',
        ),
        migrations.AddField(
            model_name='player',
            name='personal_id',
            field=models.CharField(default=0, max_length=10, verbose_name='Персональный номер'),
            preserve_default=False,
        ),
    ]
