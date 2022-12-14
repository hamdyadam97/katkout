from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView
from user import serializer
from user.models import User
from django.utils.decorators import method_decorator
from drf_yasg.openapi import IN_QUERY, Parameter
from drf_yasg.utils import swagger_auto_schema


@method_decorator(name='post', decorator=swagger_auto_schema(
    operation_description="""
    This endpoint is used to signup a new user.
    NOTE: to upload the image you need to pass it as a avatar parameter with the data
    """,
    manual_parameters=[
        Parameter('avatar', IN_QUERY,
                  'you can upload your image here',
                  type='file')
    ],
))
class SignupView(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = serializer.SignupSerializer

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(email__iexact=request.data.get('email', ''))
        return self.create(request, *args, **kwargs)


class LoginView(TokenObtainPairView):
    serializer_class = serializer.LoginSerializer