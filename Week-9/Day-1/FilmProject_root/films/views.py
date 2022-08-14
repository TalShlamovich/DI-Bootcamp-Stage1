from django.shortcuts import render
from .models import Film, Director, Country, Category
from .forms import AddDirectorForm, AddFilmForm, AddCountryForm
# Create your views here.


def homepage(request):
    return render(request, 'homepage.html')


def addDirector(request):

    context = {'form': AddDirectorForm}

    if request.method == 'POST':
        director_form = AddDirectorForm(request.POST)
        if director_form.is_valid():
            filled_form = director_form.save()

    return render(request, 'director/addDirector.html', context)

def addCountry(request):

    context = {'form': AddCountryForm}

    if request.method == 'POST':
        country_form = AddCountryForm(request.POST)
        if country_form.is_valid():
            filled_form = country_form.save()

    return render(request, 'country/addCountry.html', context)

def addFilm(request):

    context = {'form': AddFilmForm}

    if request.method == 'POST':
        film_form = AddFilmForm(request.POST)
        if film_form.is_valid():
            filled_form = film_form.save()

    return render(request, 'film/addFilm.html', context)
    