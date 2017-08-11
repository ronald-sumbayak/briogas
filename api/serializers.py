from django.contrib.auth.models import User
from rest_framework import serializers

from api import models

class DataSerializer (serializers.ModelSerializer):
    class Meta:
        model  = models.Data
        fields = '__all__'
