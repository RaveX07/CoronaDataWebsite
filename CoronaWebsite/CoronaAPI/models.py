from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=100)
    incidence = models.DecimalField(max_digits=4)
    cases = models.IntegerField(max_length=6)
    deaths = models.IntegerField(max_length=4)
