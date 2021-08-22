from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from fees.teams.models import Team
from fees.teams.serializers import TeamSerializer, TeamListSerializer, TeamRetrieveSerializer


class TeamViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list':
            return TeamListSerializer
        elif self.action == 'retrieve':
            return TeamRetrieveSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        return Team.objects.filter(players__in=[self.request.user])

    def perform_create(self, serializer):
        if "players" not in serializer.validated_data:
            serializer.validated_data["players"] = [str(self.request.user.id)]
        elif self.request.user.id not in serializer.validated_data["players"]:
            serializer.validated_data["players"].append(str(self.request.user.id))

        if "admins" not in serializer.validated_data:
            serializer.validated_data["admins"] = [str(self.request.user.id)]
        elif self.request.user.id not in serializer.validated_data["admins"]:
            serializer.validated_data["admins"].append(str(self.request.user.id))

        return super().perform_create(serializer)

