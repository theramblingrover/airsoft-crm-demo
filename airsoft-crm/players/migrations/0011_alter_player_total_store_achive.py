# Generated by Django 4.2 on 2023-04-20 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0010_alter_player_total_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='total_store',
            field=models.IntegerField(default=0, verbose_name='Сумма покупок в магазине'),
        ),
        migrations.CreateModel(
            name='Achive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('valid_time', models.DateField(null=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='achives', to='players.player')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
