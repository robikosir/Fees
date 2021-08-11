from django.db import models

from fees.fees.models import Fee
from fees.users.models import User


class Team(models.Model):
    name = models.CharField('Name', max_length=128)
    players = models.ManyToManyField(User, related_name='player_team', blank=True)
    fees = models.ManyToManyField(Fee, related_name='fee_team', blank=True)

    currency = models.CharField('Currency', max_length=128)

    def __str__(self):
        return self.name

