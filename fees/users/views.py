from rest_framework import viewsets, mixins
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from fees.users.models import User
from fees.users.serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (permissions.AllowAny,)
        return super().get_permissions()

    def validate(self, attrs):
        return attrs

    @action(methods=['get'], detail=False)
    def get_self(self, request):
        return Response(UserSerializer(request.user).data)
