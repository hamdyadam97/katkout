import re

from rest_framework import serializers

from client.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['national_id', 'name', 'slug', 'phone1', 'phone2', 'place', 'img']

        extra_kwargs = {
            'slug': {'read_only': True,}
        }



