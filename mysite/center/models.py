from django.db import models
from vaccine.models import Vaccine

# Create your models here.


class Center(models.Model):
    name = models.CharField(verbose_name="Storage Name",max_length=50)
    address = models.TextField(max_length=2000)
    
    def __str__(self):
        return self.name

class Storage(models.Model):
    center = models.ForeignKey(Center,on_delete = models.CASCADE)
    vaccine = models.ForeignKey(Vaccine,on_delete = models.CASCADE)
    total_quantity = models.IntegerField(default=0)
    booked_quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.center} | {self.vaccine}"

