from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from user.models import User
from django.utils.translation import gettext_lazy as _


class SignupSerializer(serializers.ModelSerializer):
    is_update = False
    refresh = serializers.CharField(read_only=True, source='token')
    access = serializers.CharField(read_only=True, source='token.access_token')
    avatar = serializers.ImageField(required=False,)

    def validate_password(self, data):
        validate_password(data)
        return data

    def validate_email(self, data):
        users = User.objects.filter(email__iexact=data)

        if self.is_update:
            users.exclude(id=self.instance.id)

        if users.exists():
            raise serializers.ValidationError(_("This email address already exists."))
        return data

    def validate_username(self, data):
        users = User.objects.filter(username__iexact=data)

        if self.is_update:
            users = users.exclude(id=self.instance.id)

        if users.exists():
            raise serializers.ValidationError(_("This username already exists."))
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'avatar', 'bio', 'display_name', 'dob', 'phone_number',
                  'refresh', 'access', 'is_email_verified', 'is_deactivated', 'gender')
        extra_kwargs = {
            'password': {'write_only': True},
            'dob': {'required': True},
            'gender': {'required': True}
        }


class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        try:
            super().validate(attrs)
        except AuthenticationFailed as ex:
            raise serializers.ValidationError(_("Incorrect email or password"))
        return SignupSerializer(instance=self.user, context=self.context).data