from rest_framework import serializers
from .models import Vehicles, ParkingSlot, ParkingLot, Floor, Ticket

# Creating serializers

class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicles
        fields = '__all__'

class ParkingslotSerializer():

    class Meta:
        model = ParkingSlot
        fields = '__all__'

class FloorSerializer(serializers.ModelSerializer):


    class Meta:
        model = Floor
        fields = '__all__'

class ParkingLotSerializer(serializers.ModelSerializer):


    class Meta:
        model = ParkingLot
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = '__all__'
