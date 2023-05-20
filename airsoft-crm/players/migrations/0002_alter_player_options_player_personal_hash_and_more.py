# Generated by Django 4.2 on 2023-04-10 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'verbose_name': 'Игрок', 'verbose_name_plural': 'Игроки'},
        ),
        migrations.AddField(
            model_name='player',
            name='personal_hash',
            field=models.CharField(default=0, max_length=200, verbose_name='Машиночитаемый ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='Персональный номер',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
