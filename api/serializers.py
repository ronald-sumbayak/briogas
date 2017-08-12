import datetime
from django.contrib.auth.models import User
from rest_framework import serializers

from api import models

class FullDataSerializer (serializers.ModelSerializer):
    owner = serializers.ReadOnlyField (source = 'owner.username')
    methane = serializers.ReadOnlyField (source = 'data.methane')
    oxygen = serializers.ReadOnlyField (source = 'data.oxygen')
    pressure = serializers.ReadOnlyField (source = 'data.pressure')
    content = serializers.ReadOnlyField (source = 'data.content')
    residu = serializers.ReadOnlyField (source = 'data.residu')
    katup = serializers.ReadOnlyField (source = 'data.katup')
    today_methane_production = serializers.ReadOnlyField (source = 'data.today_methane_production')
    
    class Meta:
        model  = models.Alat
        fields = '__all__'

class DataSerializer (serializers.ModelSerializer):
    class Meta:
        model  = models.Data
        fields = '__all__'
