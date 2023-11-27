from django.db import models


# Feedback models .

class Feedback(models.Model):
    first_name = models.CharField(max_length=255,blank=False)
    last_name = models.CharField(max_length=255,blank=False)
    email = models.EmailField()
    category = models.CharField(max_length=255,blank=False)
    message = models.TextField()
    attachment = models.FileField(upload_to='feedback_attchments/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.category
