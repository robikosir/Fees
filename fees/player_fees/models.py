from datetime import datetime

from django.db import models

from fees.fees.models import Fee
from fees.teams.models import Team
from fees.users.models import User


class PlayerFees(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player_fees_player')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='player_fees_team')
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE, related_name='player_fees_fee')
    time = models.DateField(default=datetime.now)
