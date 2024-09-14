from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'phone_number', 'company')
    search_fields = ('name', 'last_name', 'email', 'company')

admin.site.register(Contact, ContactAdmin)