from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Alat (models.Model):
    owner = models.OneToOneField (User)
    
    def __str__ (self):
        return "%s (id = %d)" % (self.owner.__str__ (), self.id)

class Data (models.Model):
    KATUP_OPEN = True
    KATUP_CLOSED = False
    KATUP_CHOICES = ((KATUP_OPEN, "Buka"), (KATUP_CLOSED, "Tutup"))
    
    alat = models.OneToOneField (Alat)
    methane = models.IntegerField (default = 0)
    oxygen = models.IntegerField (default = 0)
    katup = models.BooleanField (choices = KATUP_CHOICES, default = KATUP_CLOSED)
    
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
