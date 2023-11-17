from django.db import models

# Create your models here.
class Blog (models.Model):
   title = models.CharField(max_length=200)
   content = models.TextField()
   status = models.CharField(max_length=50)
   category = models.CharField()
   writer = models.CharField(max_length=100)
   created_at = models.DateTimeField(auto_now=True)
   updated_at = models.DateTimeField(auto_now=True)

class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    year_of_birth = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField()
    country = models.CharField(max_length=50, default='Kenya')
    county = models.CharField(max_length=50)
    sub_county = models.CharField(max_length=50)





   
    
    
    
    
    
    

