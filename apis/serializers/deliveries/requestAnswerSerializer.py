from rest_framework import serializers

from deliveries.models import RequestAnswer


class RequestAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestAnswer
        fields = ('delivery', 'data_delivery', 'request', 'offer_price', 'description', 'state')