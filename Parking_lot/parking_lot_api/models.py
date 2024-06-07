from django.db import models

# Types of Vehicle

VEH = [
        ('bike', 'Bike'),
        ('car', 'Car'),
        ('truck', 'Truck')
    ]

# Create your models here.
class Vehicles(models.Model):

    v_type = models.CharField(max_length=10, choices =VEH)
    reg_no = models.CharField(max_length=10, unique=True)
    color = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.reg_no}"

class ParkingSlot(models.Model):

    slot_type = models.CharField(max_length=10, choices=VEH)
    slot_number = models.IntegerField()
    is_occupied = models.BooleanField(default=False)
    vehicle = models.ForeignKey(Vehicles, on_delete=models.SET_NULL, null=True, blank=True)

    # class meta:
    #     unique = ('slot_type', 'slot_number')

    def __str__(self):
        return f"{self.slot_type} Slot {self.slot_number}"

class Floor(models.Model):

    floor_number = models.IntegerField()
    slots = models.ManyToManyField(ParkingSlot)

    def __str__(self):
        return f"Floor {self.floor_number}"

class ParkingLot(models.Model):

    parking_lot_id = models.CharField(max_length=10, unique=True)
    floors = models.ManyToManyField(Floor)

    def __str__(self):
        return f"Parking Lot  {self.parking_lot_id}"

class Ticket(models.Model):

    ticket_id = models.CharField(max_length=15, unique=True)
    vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)

    def __str__(self):
        return self.ticket_id