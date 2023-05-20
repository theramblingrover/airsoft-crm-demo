# Generated by Django 4.2 on 2023-04-12 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0005_rename_birhday_player_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='player',
            name='personal_hash',
            field=models.CharField(max_length=200, unique=True, verbose_name='Машиночитаемый ID'),
        ),
        migrations.AlterField(
            model_name='player',
            name='personal_id',
            field=models.CharField(max_length=10, unique=True, verbose_name='Персональный номер'),
        ),
    ]