from django.shortcuts import render
from rest_framework.decorators import parser_classes
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated

from bill.models import Bill
from bill.serializer import BillSerializer


@parser_classes((MultiPartParser,))
class BillView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BillSerializer

    def get_queryset(self):
        return Bill.objects.filter(client=self.request.get('client')).order_by('data_payment')