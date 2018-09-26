from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from ...serializers import RequestSerializer
from deliveries.models import Request
from users.models import Customer

class RequestViewSet(APIView):
    serializer_class = RequestSerializer
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, format=None):

        serializer = RequestSerializer(data=request.data)

        try:
            if serializer.is_valid(raise_exception=True):
                request = serializer.save()
                return Response(dict(status='done', details=serializer.data), status=200)

        except Exception as e:

            return Response(dict(status='error', details=str(e)), status=400)


class RequestList(APIView):
    serializer_class = RequestSerializer
    permission_classes = ()
    authentication_classes = ()


    def get(self, request, format=None):
        try:
            requests = Request.objects.all()
            size = len(requests)
            requests_list=[]*size
            serializer = RequestSerializer(requests, many=True)
            return Response(dict(status='done', details=serializer.data), status=200)


        except Exception as e:
            return Response(dict(status='error', details=str(e)), status=400)
