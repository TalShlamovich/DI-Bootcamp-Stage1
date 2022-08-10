from django.urls import path
from .views import todo, display


urlpatterns = [
    path("todo", todo, name='todo'),
    path("display", display, name='display')

]