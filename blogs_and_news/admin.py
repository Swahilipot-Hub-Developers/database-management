from django.contrib import admin
from .models import UserProfile,Category,Article,ArticleAnalytic,SharedArticle
from import_export.admin import ImportExportModelAdmin

class UserProfileAdmin(ImportExportModelAdmin):
    # Define the fields to display in the table
    list_display = ('user','role','bio')
    skip_unchanged = True  # Skip rows that are already present in the database
# Register the UserProfile model with the UserprofileAdmin class
admin.site.register(UserProfile,UserProfileAdmin)

class CategoryAdmin(ImportExportModelAdmin):
    # Define the fields to display in the table
    list_display = ('name','description')
    skip_unchanged = True  # Skip rows that are already present in the database
# Register the Category model with the CategoryAdmin class
admin.site.register(Category,CategoryAdmin)

class ArticleAdmin(ImportExportModelAdmin):
    # Define the fields to display in the table
    list_display = ('id','title','content','status','category','writer','created_at','updated_at','views','shares')
    skip_unchanged = True  # Skip rows that are already present in the database
    def writer_name(self, obj):
        return obj.writer.userprofile.name if obj.writer.userprofile else ''

    writer_name.short_description = 'Writer Name'
# Register the Article model with the ArticleAdmin class
admin.site.register(Article,ArticleAdmin)

class ArticleAnalyticsAdmin(ImportExportModelAdmin):
    # Define the fields to display in the table
    list_display = ('article','views','shares')
    skip_unchanged = True  # Skip rows that are already present in the database
# Register the ArticleAnalytics model with the  ArticleAnalyticsAdmin class
admin.site.register(ArticleAnalytic,ArticleAnalyticsAdmin)

class SharedArticleAdmin(ImportExportModelAdmin):
    # Define the fields to display in the table
    list_display = ('id','article','shared_at')
    skip_unchanged = True  # Skip rows that are already present in the database
# Register the SharedArticle model with the SharedArticleAdmin class
admin.site.register(SharedArticle,SharedArticleAdmin)


