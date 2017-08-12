import datetime
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Alat (models.Model):
    owner = models.OneToOneField (User)
    
    def __str__ (self):
        return "%s (id = %d)" % (self.owner.__str__ (), self.id)

class MethaneProduction (models.Model):
    alat = models.ForeignKey (Alat)
    value = models.IntegerField (default = 0)
    date = models.DateField (auto_now_add = True)
    
    def __str__ (self):
        return "%s (id = %d, date = %s)" % (self.alat.owner.__str__ (), self.alat.id, self.date)

class Data (models.Model):
    KATUP_OPEN = True
    KATUP_CLOSED = False
    KATUP_CHOICES = ((KATUP_OPEN, "Buka"), (KATUP_CLOSED, "Tutup"))
    
    alat = models.OneToOneField (Alat)
    methane = models.IntegerField (default = 0)
    oxygen = models.IntegerField (default = 0)
    pressure = models.IntegerField (default = 0)
    content = models.IntegerField (default = 0)
    residu = models.IntegerField (default = 0)
    katup = models.BooleanField (choices = KATUP_CHOICES, default = KATUP_CLOSED)
    
    @property
    def today_methane_production (self):
        instance, created = MethaneProduction.objects.get_or_create (alat = self.alat)
        return instance.value
    
    def __str__ (self):
        return "%s (id = %d)" % (self.alat.owner.__str__ (), self.alat.id)

@receiver (post_save, sender = User)
def create_user (sender, instance, created, **kwargs):
    if created:
        Token.objects.create (user = instance)
        Alat.objects.create (owner = instance)

@receiver (post_save, sender = Alat)
def create_alat (sender, instance, created, **kwargs):
    if created:
        Data.objects.create (alat = instance)
