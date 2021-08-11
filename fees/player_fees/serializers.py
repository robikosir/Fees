from rest_framework import serializers

from fees.fees.models import Fee
from fees.player_fees.models import PlayerFees
from fees.teams.models import Team
from fees.users.models import User


class PlayerFeesSerializer(serializers.ModelSerializer):
    player = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    fee = serializers.PrimaryKeyRelatedField(queryset=Fee.objects.all())

    class Meta:
        model = PlayerFees
        fields = ['id', 'player', 'team', 'fee']
        depth = 2


