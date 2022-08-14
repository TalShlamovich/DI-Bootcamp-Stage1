from django.db import models
from django.urls import reverse


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length = 80)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)


class VehicleType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class VehicleSize(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Vehicle(models.Model):
    type = models.ForeignKey(VehicleType, on_delete=models.PROTECT, related_name='type')
    date_created = models.DateField(auto_now_add=True)
    real_cost = models.BigIntegerField()
    size = models.ForeignKey(VehicleSize, on_delete = models.PROTECT, related_name='size')

    def __str__(self) -> str:
        return self.type + " " + self.size
    
    def get_absolute_url(self):
        return reverse('vehicle', args = [self.id])

class Rental(models.Model):
    rental_date = models.DateField()
    return_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='customer')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT, related_name='vehicle')

class RentalRate(models.Model):
    daily_rate = models.FloatField()
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.PROTECT, related_name='vehicle_type')
    vehicle_size = models.ForeignKey(VehicleSize, on_delete = models.PROTECT, related_name='vehicle_size')



# script to populate Customers with faker

# import faker as fk
# from rent.models import Customer

# for i in range(100):
#     i = fk()
#     fname = i.first_name()
#     lname = i.last_name()
#     e = i.email(f"{fname}{lname}@{i.domain_name()}")
#     ph = i.phone_number()
#     ad = i.address()
#     ci = i.city()
#     co = i.country()
#     Customer.objects.create(first_name = fname, last_name = lname, email = e, phone_number = ph, address = ad, city = ci, country = co)


