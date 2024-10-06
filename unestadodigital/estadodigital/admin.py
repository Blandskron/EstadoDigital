from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'phone_number', 'company', 'position', 'region', 'get_tracks')
    search_fields = ('name', 'last_name', 'email', 'company', 'region')
    list_filter = ('region', 'data_sharing_consent')  
    

    def get_tracks(self, obj):
        return ", ".join(obj.track_of_interest) 
    get_tracks.short_description = 'Tracks seleccionados'
    

    fields = (
        'name', 'last_name', 'rut', 'email', 'phone_number', 'company', 
        'position', 'region', 'track_of_interest', 'data_sharing_consent'
    )

admin.site.register(Contact, ContactAdmin)