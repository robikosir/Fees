from rest_framework import serializers

from fees.teams.models import Team
from fees.users.models import User
from fees.users.serializers import UserSerializer


class TeamSerializer(serializers.ModelSerializer):
    players = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'players']
        depth = 2


class TeamListSerializer(serializers.ModelSerializer):
    players = UserSerializer(many=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'players']
        depth = 2


