from django.db import models

from fees.fees.models import Fee
from fees.teams.models import Team
from fees.users.models import User


class PlayerFees(models.Model):
    player = models.OneToOneField(User, on_delete=models.CASCADE, related_name='player_fees_player')
    team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='player_fees_team')
    fee = models.OneToOneField(Fee, on_delete=models.CASCADE, related_name='player_fees_fee')

    class Meta:
        unique_together = (("player", "team"),)
