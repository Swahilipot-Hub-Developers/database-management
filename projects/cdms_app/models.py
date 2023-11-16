from django.db import models

# Create your models here.
class Blog (models.Model):
   title = models.CharField(max_length=200)
   content = models.TextField()
   status = models.CharField(max_length=50, default="Pending")
   category = models.CharField()
   writer = models.TextField(max_length=100)
   created_at = models.DateTimeField(auto_now=True)
   updated_at = models.DateTimeField(auto_now=True)
   
    
    
    
    
    
    

