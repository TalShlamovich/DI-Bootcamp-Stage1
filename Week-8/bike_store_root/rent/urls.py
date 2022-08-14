from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('add-vehicle', add_vehicle, name = 'add_vehicle'),
    path('add-vehicle-type', add_vehicle_type, name = 'add-vehicle-type'),
    path('add-vehicle-size', add_vehicle_size, name = 'add-vehicle-size'),
    path('vehicle/<int:id>', show_vehicle, name = 'vehicle'),
    path('vehicles', show_vehicles, name = 'show_vehicles'),

]