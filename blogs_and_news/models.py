from django.db import models

class Blogs(models.Model):
    name = models.CharField(verbose_name="Name", max_length=250)
