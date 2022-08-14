from .views import homepage, addCountry, addDirector, addFilm
from django.urls import path, include

urlpatterns = [
path('homepage', homepage, name = 'homepage'),
path('addFilm', addFilm, name = 'addFilm'),
path('addDirector', addDirector, name = 'addDirector'),
path('addCountry', addCountry, name = 'addCountry'),
]