from django.db import models


class Address(models.Model):
    house_name = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    pin_code = models.PositiveIntegerField()