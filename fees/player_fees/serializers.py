from rest_framework import serializers

from fees.fees.models import Fee
from fees.fees.serializers import FeeSerializer
from fees.player_fees.models import PlayerFees
from fees.teams.models import Team
from fees.users.models import User
from fees.users.serializers import UserSerializer


class PlayerFeesSerializer(serializers.ModelSerializer):
    player = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    fee = serializers.PrimaryKeyRelatedField(queryset=Fee.objects.all())

    class Meta:
        model = PlayerFees
        fields = ['id', 'player', 'team', 'fee', 'time']


class PlayerFeesCreateSerializer(serializers.ModelSerializer):
    players = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    fees = serializers.PrimaryKeyRelatedField(queryset=Fee.objects.all(), many=True)

    class Meta:
        model = PlayerFees
        fields = ['id', 'players', 'team', 'fees', 'time']


class PlayerFeesDetailSerializer(serializers.ModelSerializer):
    player = UserSerializer()
    team = serializers.SerializerMethodField()
    fee = FeeSerializer()

    class Meta:
        model = PlayerFees
        fields = '__all__'

    def get_team(self, obj):
        return {
            "id": obj.team.id,
            "name": obj.team.name
        }


class TeamFeeDetailSerializer(serializers.ModelSerializer):
    fee = FeeSerializer()
    player = UserSerializer()

    class Meta:
        model = PlayerFees
        fields = ['id', 'player', 'fee', 'time']

