from django.contrib import admin

# Register your models here.

from .models import Destination, Cruise, InfoRequest

admin.site.register(Destination)
admin.site.register(Cruise)
admin.site.register(InfoRequest)