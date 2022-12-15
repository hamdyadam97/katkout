from rest_framework import serializers
from bill.models import Bill


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['user', 'client', 'payment', 'remaining_amount', 'data_payment', 'data_remaining_amount', 'slug']
        extra_kwargs = {
            'slug':{'read_only': True},
        }