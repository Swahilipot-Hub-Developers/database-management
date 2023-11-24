# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ArticleAnalytic, Article

@receiver(post_save, sender=ArticleAnalytic)
def update_article_fields(sender, instance, **kwargs):
    article = instance.article
    article.views = instance.views
    article.shares = instance.shares
    article.save()
