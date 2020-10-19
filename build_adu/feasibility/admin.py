from django.contrib.gis import admin
from .models import PotentialAduParcels

# Register your models here.
admin.site.register(PotentialAduParcels, admin.OSMGeoAdmin)
