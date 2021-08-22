from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from fees.player_fees.models import PlayerFees
from fees.player_fees.serializers import PlayerFeesSerializer, PlayerFeesDetailSerializer


class PlayerFeesViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = PlayerFeesSerializer
    queryset = PlayerFees.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return PlayerFeesDetailSerializer
        return super().get_serializer_class()
