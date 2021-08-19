from rest_framework import serializers

from fees.fees.models import Fee
from fees.fees.serializers import FeeSerializer
from fees.player_fees.models import PlayerFees
from fees.teams.models import Team
from fees.teams.serializers import TeamSerializer
from fees.users.models import User
from fees.users.serializers import UserSerializer


class PlayerFeesSerializer(serializers.ModelSerializer):
    player = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    fee = serializers.PrimaryKeyRelatedField(queryset=Fee.objects.all())

    class Meta:
        model = PlayerFees
        fields = ['id', 'player', 'team', 'fee', 'time']
        depth = 2


class PlayerFeesListSerializer(serializers.ModelSerializer):
    player = UserSerializer()
    team = TeamSerializer()
    fee = FeeSerializer()

    class Meta:
        model = PlayerFees
        fields = '__all__'
        depth = 2


