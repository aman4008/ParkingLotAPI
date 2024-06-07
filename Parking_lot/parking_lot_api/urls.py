from django.urls import path
from .views import create_parking_lot,add_floor, add_parking_slot, park_vehicle, unpark_vehicle, free_slot_count, free_slots, occupied_slots

urlpatterns = [
    path('create_parking_lot/', create_parking_lot),
    path('add_floor/', add_floor),
    path('add_parking_slot/<int:floor_number>/', add_parking_slot, name='add_parking_slot'),
    path('park_vehicle/', park_vehicle),
    path('unpark_vehicle/', unpark_vehicle),
    path('free_slot_count/<str:vehicle_type>/', free_slot_count),
    path('free_slots/<str:vehicle_type>/', free_slots),
    path('occupied_slots/<str:vehicle_type>/', occupied_slots)
]