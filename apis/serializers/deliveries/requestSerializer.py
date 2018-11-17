from rest_framework import serializers

from deliveries.models import Request


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('type', 'willing_pay', 'data_customer', 'customer', 'description', 'latitud', 'longitud', 'state')
    