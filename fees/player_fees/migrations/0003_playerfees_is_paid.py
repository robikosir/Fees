# Generated by Django 3.2.3 on 2021-09-08 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player_fees', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerfees',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]