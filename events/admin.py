from django.contrib import admin
from .models import Event
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class EventsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
     list_display=('id','name','venue','event_type','description','event_date','event_time')

admin.site.register(Event,EventsAdmin)
