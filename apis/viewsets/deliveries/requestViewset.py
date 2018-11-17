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

class RequestUpdateViewSet(APIView):
    serializer_class = RequestSerializer
    permission_classes = ()
    authentication_classes = ()

    def put(self, request, format=None, pk=None, state=None):
        try:
            respuesta = Request.objects.get(id=pk)
            print(state)
            if str(state)=='2':
                print('entra')
                respuesta.state = 'proceso'
                respuesta.save()

            elif str(state)=='3':
                respuesta.state = 'realizada'
                respuesta.save()
            dictionary = dict(customer=respuesta.customer.id,
                                type=respuesta.type, 
                                 description=respuesta.description,
                                 willing_pay=respuesta.willing_pay, 
                                 latitud=respuesta.latitud, 
                                 longitud=respuesta.longitud, 
                                 state=respuesta.state
            )
            serializer = RequestSerializer(data=dictionary)

            if serializer.is_valid(raise_exception=True):
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
            print("aca esta el id", requests[0].id)
            serializer = RequestSerializer(requests, many=True)
            return Response(dict(status='done', details=serializer.data), status=200)


        except Exception as e:
            return Response(dict(status='error', details=str(e)), status=400)
