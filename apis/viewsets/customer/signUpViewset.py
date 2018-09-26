from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from rest_framework import generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from ...serializers import CustomerSerializer
from users.models import Customer

class CustomerViewSet(APIView):
    serializer_class = CustomerSerializer
    permission_classes = ()

    def post(self, request, format=None):

        serializer = CustomerSerializer(data=request.data)

        try:
            if serializer.is_valid(raise_exception=True):
                customer = serializer.save()
                return Response(dict(status='done', details=serializer.data), status=200)

        except Exception as e:

            return Response(dict(status='error', details=str(e)), status=400)