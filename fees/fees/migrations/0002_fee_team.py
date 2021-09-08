# Generated by Django 3.2.3 on 2021-08-24 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
        ('fees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fee',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_fees', to='teams.team'),
        ),
    ]