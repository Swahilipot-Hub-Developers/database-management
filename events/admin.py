from django.contrib import admin
from .models import Event,EventTicket
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class EventsAdmin(ImportExportModelAdmin):
     list_display=('id','name','description','event_date','event_duration_value','event_duration_unit','venue','organizer','banner','tickets')
     skip_unchanged = True  # Skip rows that are already present in the database
admin.site.register(Event,EventsAdmin)

class EventTicketAdmin(ImportExportModelAdmin):
     list_display=('id','ticket_no','event','ticket_type','quantity','payment_method','amount')
     skip_unchanged = True
admin.site.register(EventTicket,EventTicketAdmin)

