# Import the admin module and the Blog model
from django.contrib import admin
from .models import Blog,Member

# Define a new class that inherits from admin.ModelAdmin
class BlogAdmin(admin.ModelAdmin):
    # Define the fields to display in the table
    list_display = ('title', 'content', 'status', 'category', 'writer', 'created_at', 'updated_at')

# Register the Blog model with the BlogAdmin class
admin.site.register(Blog, BlogAdmin)


class MemberAdmin(admin.ModelAdmin):
    list_display = ('member_id', 'name', 'gender', 'year_of_birth', 'phone_number', 'email_address', 'country', 'county', 'sub_county')

admin.site.register(Member, MemberAdmin)


