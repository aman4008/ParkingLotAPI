from django.contrib import admin
from .models import ParkingLot, Floor, ParkingSlot, Vehicles, Ticket
# Register your models here.

admin.site.register(ParkingLot)
admin.site.register(ParkingSlot)
admin.site.register(Floor)
admin.site.register(Vehicles)
admin.site.register(Ticket)