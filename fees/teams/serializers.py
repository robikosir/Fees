from rest_framework import serializers

from fees.fees.models import Fee
from fees.fees.serializers import FeeSerializer
from fees.teams.models import Team
from fees.users.models import User
from fees.users.serializers import UserSerializer


class TeamSerializer(serializers.ModelSerializer):
    players = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    fees = serializers.PrimaryKeyRelatedField(queryset=Fee.objects.all(), many=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'currency', 'players', 'fees']
        depth = 2


class TeamListSerializer(serializers.ModelSerializer):
    players = UserSerializer(many=True)
    fees = FeeSerializer(many=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'currency', 'players', 'fees']
        depth = 2


