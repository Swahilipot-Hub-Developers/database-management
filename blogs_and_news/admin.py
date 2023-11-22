from django.contrib import admin
from .models import UserProfile,Category,Article,ArticleAnalytics,SharedArticle
from import_export.admin import ImportExportModelAdmin

class UserProfileAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    # Define the fields to display in the table
    list_display = ('id','user','role','bio')
# Register the UserProfile model with the UserprofileAdmin class
admin.site.register(UserProfile,UserProfileAdmin)

class CategoryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    # Define the fields to display in the table
    list_display = ('id','name','description')
# Register the Category model with the CategoryAdmin class
admin.site.register(Category,CategoryAdmin)

class ArticleAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    # Define the fields to display in the table
    list_display = ('id','title','content','status','category','writer','created_at','updated_at')
# Register the Article model with the ArticleAdmin class
admin.site.register(Article,ArticleAdmin)

class ArticleAnalyticsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    # Define the fields to display in the table
    list_display = ('id','article','views','shares')
# Register the ArticleAnalytics model with the  ArticleAnalyticsAdmin class
admin.site.register(ArticleAnalytics,ArticleAnalyticsAdmin)

class SharedArticleAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    # Define the fields to display in the table
    list_display = ('id','article','ip_address','shared_at')
# Register the SharedArticle model with the SharedArticleAdmin class
admin.site.register(SharedArticle,SharedArticleAdmin)


