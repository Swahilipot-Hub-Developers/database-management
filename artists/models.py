from django.db import models
from django.contrib.auth.models import User



class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="artist")
    type = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    skills = models.CharField(max_length=64)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.user.user


