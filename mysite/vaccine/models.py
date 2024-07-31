from django.db import models

# Create your models here.

class Vaccine(models.Model):
    name = models.CharField(verbose_name="Vaccine Name",max_length=50)
    description = models.TextField(max_length=2000)
    number_of_doses = models.IntegerField(default=1)
    interval = models.IntegerField(default=0,help_text="Please provide interval in days.")
    storage_temperature = models.IntegerField(null=True,blank=True,help_text="Provide the temperature in Celcius.")
    minimum_age = models.IntegerField(default=0)

    def __str__(self):
        return self.name
