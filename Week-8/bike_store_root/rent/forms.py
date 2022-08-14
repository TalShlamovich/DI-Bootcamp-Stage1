from django import forms
from .models import *


class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = '__all__'

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

        
class VehicleTypeForm(forms.ModelForm):
    class Meta:
        model = VehicleType
        fields = '__all__'


class VehicleSizeForm(forms.ModelForm):
    class Meta:
        model = VehicleSize
        fields = '__all__'


class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = '__all__'


class RentalRateForm(forms.ModelForm):
    class Meta:
        model = RentalRate
        fields = '__all__'

