from django.db import models

from fees.teams.models import Team


class Fee(models.Model):
    name = models.CharField('Name', max_length=128)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_fees')
    price = models.FloatField()

    def __str__(self):
        return self.name
