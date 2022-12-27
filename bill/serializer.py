from rest_framework import serializers
from bill.models import Bill, PurchaseOfGoods


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['user', 'client', 'payment', 'remaining_amount', 'data_payment', 'data_remaining_amount', ]



class PurchaseOfGoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOfGoods
        fields = ['id','user','client','bill','name','number','price',]

