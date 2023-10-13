from django.contrib import admin

# Register your models here.

from .models import Destination, Cruise

admin.site.register(Destination)
admin.site.register(Cruise)