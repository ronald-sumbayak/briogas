from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api import serializers, models

@api_view (['GET'])
def retrieve_data (request):
    data = models.Data.objects.get (alat__owner = request.user)
    serializer = serializers.DataSerializer (data)
    return Response (serializer.data)

class UpdateData (generics.UpdateAPIView):
    serializer_class = serializers.DataSerializer
    queryset = models.Data.objects.all ()
    
    def get_object (self):
        if self.request.data.get ('id'):
            return self.queryset.get (id = self.request.data['id'])
        raise ValidationError ("id must be provided", "required")

@api_view (['POST', 'PATCH'])
@permission_classes ([IsAuthenticated])
def toggle_katup (request):
    data = models.Data.objects.get (alat__owner = request.user)
    data.katup = not data.katup
    data.save ()
    serializer = serializers.DataSerializer (data)
    return Response (serializer.data)
