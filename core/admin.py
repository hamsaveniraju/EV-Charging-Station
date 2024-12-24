from django.contrib import admin
from .models import EVChargingLocation

class EVChargingLocationAdmin(admin.ModelAdmin):
    list_display = ('station_name', 'latitude', 'longitude')  # Use correct field names
    list_filter = ('station_name',)  # Use correct field names for filtering

admin.site.register(EVChargingLocation, EVChargingLocationAdmin)
