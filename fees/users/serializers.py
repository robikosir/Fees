from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from fees.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request', None)
        method = getattr(request, 'method', None)

        if request and method in ['PATCH', 'PUT']:
            fields['password'].required = False

        return fields


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
