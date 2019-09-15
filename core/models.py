from django.db import models

# Create your models here.

class dataSet(models.Model):
    dataID = models.IntegerField()
    data = models.CharField(max_length=100)