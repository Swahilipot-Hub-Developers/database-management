from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Artist

class ArtistAdmin(ImportExportModelAdmin):
    list_display=('id','user','type','description','skills','photo')
    skip_unchanged = True  # Skip rows that are already present in the database
    
admin.site.register(Artist,ArtistAdmin)





