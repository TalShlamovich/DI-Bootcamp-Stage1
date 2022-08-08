from django.shortcuts import render
from django.http import HttpResponse
from .models import UserProfile, Posts




# Create your views here.
def index(request):

    return HttpResponse("this is index")

def profile (request):

   return HttpResponse("this is profile")


def posts(request, author_id: int) -> HttpResponse:
    user = UserProfile.objects.get(id = author_id)
    posts = user.posts.all()

    return render(request, 'posts.html', {'posts': posts})