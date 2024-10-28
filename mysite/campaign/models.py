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
    
    def is_reserved(self,campaign_id,slot_id):
        from center.models import Storage 
        from django.db.models import F
        
        slot = Slot.objects.get(id=slot_id)
        campaign = Campaign.objects.get(id=campaign_id)
        storage = Storage.objects.get(vaccine=campaign.vaccine,center = campaign.center)
        
        if (storage.total_quantity > 0) and (storage.total_quantity > storage.booked_quantity) and (slot.max_capacity > 0) and (slot.max_capacity > slot.reserved):
            slot.reserved = F("reserved") + 1
            storage.booked_quantity = F("booked_quantity") + 1
            slot.save()
            storage.save()
            return True
        return False
        
        