from django.db import models
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType


# User Profile to differentiate a writer and admin with role
class UserProfile(models.Model):
         ROLE_CHOICES = [
            ('writer', 'Writer'),
           
        ]
         user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,unique=True,verbose_name="User")
         role = models.CharField(max_length=50,choices=ROLE_CHOICES, default='writer') #This will take 'writer' or 'admin'
         bio = models.TextField(blank=True)

         def __str__(self):
           return self.user

# Category model for managing article categories
class Category(models.Model):
    name = models.CharField(max_length=99, unique=True,primary_key=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
   

# Article model for storing blogs and News article 
class Article(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Published', 'Published'),
        ('Draft', 'Draft')
    )

    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES ,default="Pending")
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'userprofile__role': 'writer'})
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0,editable=False)
    shares = models.PositiveIntegerField(default=0,editable=False)
    def __str__(self):
        return self.title

    

# ArticleAnalytics  model for storing article analytics data 
class ArticleAnalytic(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    shares = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.article


class SharedArticle(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    shared_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.article