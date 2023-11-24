from django.contrib import admin
from .models import Feedback
from import_export.admin import ImportExportModelAdmin


class FeedbackAdmin(ImportExportModelAdmin):
    list_display=('id','first_name','last_name','email','category','message','attachment','timestamp')
    skip_unchanged = True  # Skip rows that are already present in the database
admin.site.register(Feedback,FeedbackAdmin)