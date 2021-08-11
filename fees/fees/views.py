from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from fees.fees.models import Fee
from fees.fees.serializers import FeeSerializer


class FeeViewSet(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 viewsets.GenericViewSet):
    serializer_class = FeeSerializer
    queryset = Fee.objects.all()
    # permission_classes = (IsAuthenticated,)

