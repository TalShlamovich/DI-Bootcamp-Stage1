from django.urls import path
from .views import todo, display, complete


urlpatterns = [
    path("todo", todo, name='todo'),
    path("display", display, name='display'),
    path('/complete', complete, name='complete')
    

]