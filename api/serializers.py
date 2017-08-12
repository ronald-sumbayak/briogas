import datetime
from django.contrib.auth.models import User
from rest_framework import serializers

from api import models

class FullDataSerializer (serializers.ModelSerializer):
    owner = serializers.ReadOnlyField (source = 'owner.username')
    methane = serializers.ReadOnlyField (source = 'data.methane')
    pressure = serializers.ReadOnlyField (source = 'data.pressure')
    temperature = serializers.ReadOnlyField (source = 'data.temperature')
    power = serializers.ReadOnlyField (source = 'data.power')
    today_methane_production = serializers.ReadOnlyField (source = 'data.today_methane_production')
    
    class Meta:
        model  = models.Alat
        fields = '__all__'

class DataSerializer (serializers.ModelSerializer):
    class Meta:
        model  = models.Data
        fields = '__all__'
