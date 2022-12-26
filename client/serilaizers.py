import re

from rest_framework import serializers

from client.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id','national_id', 'name', 'phone1', 'phone2', 'place', 'img']




