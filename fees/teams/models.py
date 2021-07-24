from django.contrib.auth.models import User
from django.db import models


class Team(models.Model):
    name = models.CharField('Name', max_length=128)
    players = models.ManyToManyField(User, related_name="player_team", blank=True)
