from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from fees.teams.models import Team
from fees.teams.serializers import TeamSerializer, TeamListSerializer


class TeamViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    # permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list':
            return TeamListSerializer
        return super().get_serializer_class()
