from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from fees.player_fees.models import PlayerFees
from fees.player_fees.serializers import PlayerFeesSerializer


class PlayerFeesViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = PlayerFeesSerializer
    queryset = PlayerFees.objects.all()
    # permission_classes = (IsAuthenticated,)
