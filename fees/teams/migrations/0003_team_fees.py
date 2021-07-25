# Generated by Django 3.2.3 on 2021-07-25 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0001_initial'),
        ('teams', '0002_team_players'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='fees',
            field=models.ManyToManyField(blank=True, related_name='fee_team', to='fees.Fee'),
        ),
    ]
