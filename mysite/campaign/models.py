from django.db import models
from vaccine.models import Vaccine
from center.models import Center
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Campaign(models.Model):
    center = models.ForeignKey(Center,on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine,on_delete=models.CASCADE)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    agents = models.ManyToManyField(User,blank=True)
    
    def __str__(self):
        return f"{str(self.vaccine).upper()} | {str(self.center).upper()}"

class Slot(models.Model):
    campaign = models.ForeignKey(Campaign,on_delete=models.CASCADE)
    date = models.DateField(null=True,blank=True)
    start_time = models.TimeField(null=True,blank=True)
    end_time = models.TimeField(null=True,blank=True)
    max_capacity = models.IntegerField(null=True,blank=True,default=0)
    reserved = models.IntegerField(null=True,blank=True,default=0)
    
    def __str__(self):
        return f"{self.date} | {self.start_time} | {self.end_time}"
    
    