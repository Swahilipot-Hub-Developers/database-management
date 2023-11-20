from django.db import models

class Feedback(models.Model):
    name = models.CharField(verbose_name="Name", max_length=250)
