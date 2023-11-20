from django.db import models

class Artist(models.Model):
    name = models.CharField(verbose_name="Name", max_length=250)

class Profile(models.Model):
    name = models.CharField(verbose_name="Profile", max_length=250)
