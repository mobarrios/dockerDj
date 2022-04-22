from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.

class Clients(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Items(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()

class Req(models.Model):
    number = IntegerField()
    date = models.DateField()
    checke = models.BooleanField()

    