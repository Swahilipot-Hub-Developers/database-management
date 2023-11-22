from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Artist

class ArtistAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('id','user','type','description','skills','photo')
    
admin.site.register(Artist,ArtistAdmin)





