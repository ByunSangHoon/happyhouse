from django.db import models

# Create your models here.
class ClientInfo(models.Model):
    room_number = models.CharField(max_length=100, unique=True)
    resident_name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=100, null=True)
    price = models.PositiveIntegerField()
    real_price = models.PositiveIntegerField()
    is_usable = models.BooleanField(default=False)

    check_in_time = models.CharField(max_length=100, null=True)

    nationality = models.CharField(max_length=100, null=True)
    birth = models.CharField(max_length=100, null=True)
    ph_number = models.CharField(max_length=100, null=True)
    job = models.CharField(max_length=100, null=True)
    etc = models.TextField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)