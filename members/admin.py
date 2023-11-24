from django.contrib import admin
from .models import Member,AdminProfile
from import_export.admin import ImportExportModelAdmin

class MemberAdmin(ImportExportModelAdmin):
    # Define the fields to display in the table
    list_display = ('id','member_id','name','gender','year_of_birth','phone_number','email_address','country','county','sub_county')
    skip_unchanged = True  # Skip rows that are already present in the database
    import_id_fields = ('member_id',)  # Specify the import_id_fields
   

admin.site.register(Member,MemberAdmin)

class AdminProfileAdmin(ImportExportModelAdmin):
    list_display=('user','phone_number')
    skip_unchanged = True  # Skip rows that are already present in the database
admin.site.register(AdminProfile,AdminProfileAdmin)
