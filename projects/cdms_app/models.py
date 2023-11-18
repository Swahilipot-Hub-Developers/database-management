from django.db import models

# Create your models here.
class Blog(models.Model):
   id = models.AutoField(primary_key=True)
   title = models.CharField(max_length=200)
   content = models.TextField()
   status = models.CharField(max_length=50)
   category = models.CharField()
   writer = models.CharField(max_length=100)
   created_at = models.DateTimeField(auto_now=True)
   updated_at = models.DateTimeField(auto_now=True,editable=False)

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
class Artist(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='Attachments/artist_photos/', null=False, blank=False)

class Event(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    venue= models.CharField(max_length=100)
    date=models.DateField()
    time=models.TimeField()
    event_type = models.CharField(max_length=100)
    description = models.TextField()


class Feedback(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    category = models.CharField(max_length=255)
    message = models.TextField()
    attachment = models.FileField(upload_to='Attachments/feedback_uploads/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)









   
    
    
    
    
    
    

