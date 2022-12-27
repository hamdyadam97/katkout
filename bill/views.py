from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import parser_classes, api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from bill.models import Bill
from bill.serializer import BillSerializer, PurchaseOfGoodsSerializer


# @parser_classes((MultiPartParser,))
class BillView(CreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = BillSerializer

    def get_queryset(self):
        return Bill.objects.all().order_by('data_payment')


@parser_classes((MultiPartParser,))
class BillUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated],
    serializer_class = BillSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        return Bill.objects.all()


# @swagger_auto_schema(method='post', request_body=PurchaseOfGoodsSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated],)
def purchase_of_goods(request):
    if request.method =='POST':
        purchase_of_goods = PurchaseOfGoodsSerializer(data=request.data)
        if purchase_of_goods.is_valid():
            purchase_of_goods.save()
            return Response(data=purchase_of_goods.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data={"function must post"},status=status.HTTP_400_BAD_REQUEST)