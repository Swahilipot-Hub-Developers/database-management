from django.contrib import admin
from .models import Feedback
from import_export.admin import ImportExportModelAdmin


class FeedbackAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('id','first_name','last_name','email','category','message','attachment','timestamp')

admin.site.register(Feedback,FeedbackAdmin)