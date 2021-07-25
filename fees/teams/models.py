from django.db import models

from fees.users.models import User


class Team(models.Model):
    name = models.CharField('Name', max_length=128)
    players = models.ManyToManyField(User, related_name="player_team", blank=True)
