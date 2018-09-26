from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import Customer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Customer
        fields = ('cellphone', 'document_number', 'document_type', 'user_type', 'user')
    

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_primary_data = dict(username = user_data['username'], password = user_data['password'])
        user = User.objects.create_user(**user_primary_data)
        user.first_name = user_data['first_name']
        user.last_name = user_data['last_name']
        user.email = user_data['email']
        user.save()
        customer = Customer.objects.create(user = user, **validated_data)
        return customer