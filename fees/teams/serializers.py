from rest_framework import serializers

from fees.player_fees.serializers import TeamFeeDetailSerializer
from fees.teams.models import Team
from fees.users.models import User
from fees.users.serializers import UserSerializer


class TeamSerializer(serializers.ModelSerializer):
    players = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, required=False)
    admins = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, required=False)

    class Meta:
        model = Team
        fields = ['id', 'name', 'currency', 'players', 'admins']
        depth = 2


class TeamListSerializer(serializers.ModelSerializer):
    players = UserSerializer(many=True)
    admins = UserSerializer(many=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'currency', 'players', 'admins']


class TeamRetrieveSerializer(serializers.ModelSerializer):
    players = UserSerializer(many=True)
    admins = UserSerializer(many=True)
    player_fees_team = TeamFeeDetailSerializer(many=True)
    team_fees_total = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ['id', 'name', 'currency', 'players', 'admins', 'player_fees_team', 'team_fees_total']

    def get_team_fees_total(self, obj):
        return sum(player_fee.fee.price for player_fee in obj.player_fees_team.all())



