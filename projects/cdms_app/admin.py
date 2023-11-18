# Import the admin module 
from django.contrib import admin
# Import the Member, Event,Blog and Artist model fom models.py
from .models import Member,Event,Blog,Artist,Feedback



# Define a new class that inherits from admin.ModelAdmin
class MemberAdmin(admin.ModelAdmin):
    # Define the fields to display in the table
    list_display = ('member_id', 'name', 'gender', 'year_of_birth', 'phone_number', 'email_address', 'country', 'county', 'sub_county')
# Register the Member model with the MemberAdmin class
admin.site.register(Member, MemberAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display=('id','title','content','status','category','writer','created_at','updated_at')
admin.site.register(Blog,BlogAdmin)


class ArtisAdmin(admin.ModelAdmin):
    list_display=('id','name','type','description','photo')
admin.site.register(Artist,ArtisAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','email','category','message','attachment','timestamp')
admin.site.register(Feedback,FeedbackAdmin)



class EventsAdmin(admin.ModelAdmin):
    list_display=('name','venue','date','time','event_type','description')

admin.site.register(Event,EventsAdmin)


