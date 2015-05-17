from django.db import models

# Create your models here.
class ClientInfo(models.Model):
    room_number = models.CharField(max_length=100)
    resident_name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=4, null=True)
    price = models.PositiveIntegerField()
    real_price = models.PositiveIntegerField()
    etc = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
