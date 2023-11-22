from django.contrib import admin
from .models import Member,AdminProfile
from import_export.admin import ImportExportModelAdmin

class MemberAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    # Define the fields to display in the table
    list_display = ('member_id','name','gender','year_of_birth','phone_number','email_address','country','county','sub_county')
# Register the UserProfile model with the UserprofileAdmin class
admin.site.register(Member,MemberAdmin)

class AdminProfileAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('user','phone_number')
admin.site.register(AdminProfile,AdminProfileAdmin)
