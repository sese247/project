from django.db import models

class Seouldata(models.Model):
    sisulname = models.CharField(max_length = 50)
    sisuladdr = models.CharField(max_length=50)
    tel =  models.CharField(max_length=20)

class Datasample(models.Model):
    sisulname = models.CharField(max_length = 100)
    sisuladdr = models.CharField(max_length = 100)
    tel = models.CharField(max_length = 20)
    kind = models.CharField(max_length = 20)
    lat = models.FloatField(default=0.0)
    lng = models.FloatField(default=0.0)


class Sample(models.Model):
    name = models.CharField(max_length=100)
    addr = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    lat = models.FloatField(default=0.0)
    lng = models.FloatField(default=0.0)
    kind = models.CharField(max_length=20)
    kind_detail = models.CharField(max_length=20)
# Create your models here.
