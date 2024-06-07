from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ParkingLot, Vehicles, ParkingSlot, Floor, Ticket
from .serializers import ParkingLotSerializer,ParkingslotSerializer,FloorSerializer, VehicleSerializer, TicketSerializer

# Create your views here.
@api_view(['POST'])
def create_parking_lot(request):
    parking_lot = ParkingLot.objects.create(parking_lot_id='PR1234')
    return Response({'success': 'True', 'parking_lot_id': parking_lot.parking_lot_id})

@api_view(['POST'])
def add_floor(request):
    data = request.data
    num_slots = data.get('num_slots')
    floor_number = Floor.objects.count() + 1
    floor = Floor.objects.create(floor_number = floor_number)
    for i in range(1, num_slots + 1):
        if i == 1:
            slot_type = 'truck'
        elif 2 <= i <= 3:
            slot_type = 'bike'
        else:
            slot_type = 'car'
        slot = ParkingSlot.objects.create(slot_type=slot_type, slot_number=i)
        floor.slots.add(slot)
    parking_lot = ParkingLot.objects.get(parking_lot_id= "PR1234")
    parking_lot.floors.add(floor)
    return Response({"msg": "Added"})

@api_view(['POST'])
def add_parking_slot(request, floor_number):
    data = request.data
    slot_type = data.get("slot_type")
    floor = Floor.objects.get(floor_number= floor_number)
    slot_number = floor.slots.count()+1
    slot = ParkingSlot.objects.create(slot_type=slot_type, slot_number=slot_number)
    floor.slots.add(slot)
    return Response({"status": "added success"})

@api_view(['POST'])
def park_vehicle(request):
    data = request.data
    vehicle_serializer = VehicleSerializer(data=data)
    if vehicle_serializer.is_valid():
        vehicle = vehicle_serializer.save()
        for floor in Floor.objects.all().order_by('floor_number'):
            slot = floor.slots.filter(slot_type=vehicle.v_type, is_occupied=False).first()
            if slot:
                slot.is_occupied = True
                slot.vehicle = vehicle
                slot.save()
                ticket_id = f"{"PR1234"}_{floor.floor_number}_{slot.slot_number}"
                ticket = Ticket.objects.create(ticket_id=ticket_id,vehicle=vehicle, floor=floor, slot=slot)
                return Response({"status": "Vehicle Parked", "ticket_id": ticket_id})
        return Response({"status":"No Slot Available"})
    return Response(vehicle_serializer.errors)

@api_view(['POST'])
def unpark_vehicle(request):
    data = request.data
    ticket_id = data.get('ticket_id')
    try:
        ticket = Ticket.objects.get(ticket_id=ticket_id)
        slot = ticket.slot
        slot.is_occupied = False
        slot.vehicle = None
        slot.save()
        ticket.delete()
        return Response({"status": "vehicle Unparked"})
    except Ticket.DoesNotExist:
        return Response({"Status": "Ticket Not Found"})

@api_view(['GET'])
def free_slot_count(request, vehicle_type):
    free_slot_count = {}
    for floor in Floor.objects.all().order_by('floor_number'):
        count = floor.slots.filter(slot_type = vehicle_type, is_occupied= False).count()
        free_slot_count[floor.floor_number] = count
    return Response({"Free_slot_count":free_slot_count})

@api_view(['GET'])
def free_slots(request, vehicle_type):
    free_slots = {}
    for floor in Floor.objects.all().order_by('floor_number'):
        free_slots[floor.floor_number] = list(floor.slots.filter(slot_type=vehicle_type, is_occupied=False).values_list('slot_number', flat=True))
        return Response({"free_slots":free_slots})

@api_view(['GET'])
def occupied_slots(request, vehicle_type):
    occupied_slots = {}
    for floor in Floor.objects.all().order_by('floor_number'):
        occupied_slots[floor.floor_number] = list(floor.slots.filter(slot_type=vehicle_type, is_occupied=True).values_list('slot_number', flat=True))
    return Response({"occupied_slots": occupied_slots})






