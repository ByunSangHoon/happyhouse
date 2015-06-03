from django.db import models
#-*- coding: UTF-8 -*-

# Create your models here.
class ClientInfo(models.Model):

    ROOM_TYPE_CHOICES = (
        ('RT01', '외창화장실'),
        ('RT02', '내창화장실'),
        ('RT03', '내창'),
        ('RT04', '무창화장실')
    )

    room_number = models.CharField(max_length=100, unique=True)
    resident_name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=100, null=True, choices=ROOM_TYPE_CHOICES)
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