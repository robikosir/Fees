from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from fees.fees.models import Fee
from fees.fees.serializers import FeeSerializer
from fees.teams.models import Team


class FeeViewSet(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 viewsets.GenericViewSet):
    serializer_class = FeeSerializer
    queryset = Fee.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        teams = Team.objects.filter(players__in=[self.request.user])
        return Fee.objects.filter(team_id__in=teams)


