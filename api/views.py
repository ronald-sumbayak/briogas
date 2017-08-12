import datetime
from rest_framework import generics, mixins
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api import serializers, models

@api_view (['GET'])
def retrieve_data (request):
    alat = models.Alat.objects.get (owner = request.user)
    serializer = serializers.FullDataSerializer (alat)
    return Response (serializer.data)

@api_view (['POST', 'PATCH'])
def update_data (request):
    alat = get_object_or_404 (models.Alat, id = request.data['id'])
    
    data_serializer = serializers.DataSerializer (alat.data, request.data, partial = True)
    data_serializer.is_valid (raise_exception = True)
    data_serializer.save ()
    
    methane_product, created = alat.methaneproduction_set.get_or_create (
        date = datetime.date.today (), alat = alat)
    methane_product.value += int (request.data.get (
        'methane_production', methane_product.value))
    methane_product.save ()
    
    serializer = serializers.FullDataSerializer (alat)
    return Response (serializer.data)

class UpdateData (generics.GenericAPIView, mixins.UpdateModelMixin):
    serializer_class = serializers.FullDataSerializer
    queryset = models.Data.objects.all ()
    
    def post (self, request, *args, **kwargs):
        return self.partial_update (request, *args, **kwargs)
    
    def patch (self, request, *args, **kwargs):
        return self.partial_update (request, *args, **kwargs)
    
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
    serializer = serializers.FullDataSerializer (data)
    return Response (serializer.data)
