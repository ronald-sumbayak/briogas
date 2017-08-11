from django.contrib.auth.models import User
from rest_framework import serializers

from api import models

class DataSerializer (serializers.ModelSerializer):
    class Meta:
        model  = models.Data
        fields = '__all__'

class UpdateDataSerializer (serializers.ModelSerializer):
    user = serializers.HyperlinkedIdentityField ('id')
    
    class Meta:
        model  = models.Data
        fields = '__all__'
        
    def validate_user (self, value):
        try:
            User.objects.get (username = value)
            return value
        except User.DoesNotExist:
            raise serializers.ValidationError ("User does not exists")
