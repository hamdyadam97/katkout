from django.shortcuts import render
from rest_framework.decorators import parser_classes
from rest_framework.generics import CreateAPIView, ListAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated

from .models import Client
from .serilaizers import ClientSerializer


@parser_classes((MultiPartParser,))
class ClientView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ClientSerializer


@parser_classes((MultiPartParser,))
class ClientViewDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ClientSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'client_slug'
    # queryset = Client.objects.all()

    def get_queryset(self):
        return Client.objects.all()

