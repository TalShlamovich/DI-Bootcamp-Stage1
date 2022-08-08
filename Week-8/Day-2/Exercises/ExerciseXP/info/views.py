from django.shortcuts import render
from django.http import HttpResponse
from .models import Family, Animal

# Create your views here.
def family(request, family_id) -> HttpResponse:
    family = Family.objects.get(pk=family_id)
    
    return render(request, 'family.html', {'family': family})

def animals(request) -> HttpResponse:
    pass
    # return render(request, 'animals.html', ?????)

def animal(request) -> HttpResponse:
    pass
    # return render(request, 'animal.html', ?????)