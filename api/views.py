from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api import serializers, models

@api_view (['GET'])
def retrieve_data (request):
    data = models.Data.objects.get (alat__owner = request.user)
    serializer = serializers.DataSerializer (data)
    return Response (serializer.data)

@api_view (['POST', 'PATCH'])
@permission_classes ([IsAuthenticated])
def update_data (request):
    serializer = serializers.UpdateDataSerializer (data = request.data)
    serializer.save ()
    serializer.is_valid (raise_exception = True)
    serializer.save ()
    return Response (serializer.data)

@api_view (['POST', 'PATCH'])
@permission_classes ([IsAuthenticated])
def toggle_katup (request):
    data = models.Data.objects.get (alat__owner = request.user)
    data.katup = not data.katup
    data.save ()
    serializer = serializers.DataSerializer (data)
    return Response (serializer.data)
