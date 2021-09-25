from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from fees.helpers.email_helper.helper import send_fee_email
from fees.player_fees.models import PlayerFees
from fees.player_fees.serializers import PlayerFeesSerializer, PlayerFeesDetailSerializer, PlayerFeesCreateSerializer


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
        elif self.action == 'create':
            return PlayerFeesCreateSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        data = {
            "team": request.data.get("team"),
            "time": request.data.get("time"),
            "description": request.data.get("description")
        }
        send_fee_email().delay(request.data.get("players", []), request.data.get("fees", []), request.data.get("team"))
        for player in request.data.get("players", []):
            for fee in request.data.get("fees", []):
                data["player"] = player
                data["fee"] = fee
                serializer = PlayerFeesSerializer(data=data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
        return Response("created", status=status.HTTP_201_CREATED, headers=headers)
