from django.db import models

class Event(models.Model):
    name = models.CharField(verbose_name="Name", max_length=250)
    venue= models.CharField(verbose_name="Venue", max_length=250)
    event_type= models.CharField(verbose_name="EventType", max_length=250)
    description = models.TextField(verbose_name="Description")
    event_date=models.DateField(verbose_name='Date')
    event_time=models.TimeField(verbose_name="Time",default='12:00:00')
    
    
