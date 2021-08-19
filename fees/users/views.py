import copy

from rest_framework import viewsets, mixins, status
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from fees.helpers.email_helper.helper import send_invite_email
from fees.users.models import User
from fees.users.serializers import UserSerializer, ChangePasswordSerializer


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

    @action(methods=['get'], detail=False)
    def get_self(self, request):
        return Response(UserSerializer(request.user).data)

    @action(methods=['post'], detail=False)
    def invite(self, request):
        data = copy.deepcopy(request.data)
        data["password"] = User.objects.make_random_password()
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        send_invite_email([data["email"]], data["first_name"], data["password"])
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=['post'], detail=False)
    def change_password(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        self.object = request.user

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
