# Generated by Django 3.2.3 on 2021-09-25 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player_fees', '0003_playerfees_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerfees',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]