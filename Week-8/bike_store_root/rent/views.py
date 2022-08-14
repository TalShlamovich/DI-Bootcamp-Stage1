from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def add_vehicle(request):

    context = {'form': VehicleForm}

    if request.method == 'POST':
        vehicle_form = VehicleForm(request.POST)
        if vehicle_form.is_valid():
            filled_form = vehicle_form.save()


    return render(request, 'add_vehicle.html', context)

def add_vehicle_type(request):

    context = {'form': VehicleTypeForm}

    if request.method == 'POST':
        vehicle_type_form = VehicleTypeForm(request.POST)
        if vehicle_type_form.is_valid():
            filled_form = vehicle_type_form.save()


    return render(request, 'add_vehicle.html', context)

def add_vehicle_size(request):

    context = {'form': VehicleSizeForm}

    if request.method == 'POST':
        vehicle_size_form = VehicleSizeForm(request.POST)
        if vehicle_size_form.is_valid():
            filled_form = vehicle_size_form.save()


    return render(request, 'add_vehicle.html', context)


def show_vehicle(request, id):
    vehicle_chosen = Vehicle.objects.get(id=id)
    return render (request, 'show_vehicle.html', {'vehicle': vehicle_chosen})

def show_vehicles(request):
    vehicles_all = Vehicle.objects.all()
    return render (request, 'vehicles.html', {'vehicles': vehicles_all})

