from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from ...serializers import RequestAnswerSerializer
from deliveries.models import RequestAnswer

class RequestAnswerViewSet(APIView):
    serializer_class = RequestAnswerSerializer
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, format=None):

        serializer = RequestAnswerSerializer(data=request.data)

        try:
            if serializer.is_valid(raise_exception=True):
                request = serializer.save()
                return Response(dict(status='done', details=serializer.data), status=200)

        except Exception as e:

            return Response(dict(status='error', details=str(e)), status=400)


class RequestAnswerList(APIView):
    serializer_class = RequestAnswerSerializer
    permission_classes = ()
    authentication_classes = ()


    def get(self, request, format=None, pk=None):
        try:
            requests = RequestAnswer.objects.filter(request=pk)
            serializer = RequestAnswerSerializer(requests, many=True)
            return Response(dict(status='done', details=serializer.data), status=200)


        except Exception as e:
            return Response(dict(status='error', details=str(e)), status=400)