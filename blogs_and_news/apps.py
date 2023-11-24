from django.apps import AppConfig


class BlogsAndNewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogs_and_news'

    def ready(self):
        import blogs_and_news.signals  # Import blog_and_news signal module