from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'phone_number', 'company', 'region', 'get_tracks')
    search_fields = ('name', 'last_name', 'email', 'company', 'region')
    list_filter = ('region', 'data_sharing_consent')  # Filtra por región y si consintió compartir datos

    # Mostrar los tracks seleccionados en el listado de Contact
    def get_tracks(self, obj):
        return ", ".join(obj.track_of_interest)  # Como es un JSONField, accedemos directamente
    get_tracks.short_description = 'Tracks seleccionados'

admin.site.register(Contact, ContactAdmin)


"""
from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'phone_number', 'company')
    search_fields = ('name', 'last_name', 'email', 'company')

admin.site.register(Contact, ContactAdmin)
"""
