from django.shortcuts import render
from django.http import HttpResponse


person = {
    'Name': 'Yossi',
    'GitHub': 'yussieik@github.com',
    'Address': 'Israel'
}

# Create your views here.
def index(request):

    output = "Hello, this is my forst website"

    context = {'greeting': output, **person}

    return render(request, 'homepage.html', context)

def profile (request):

    user_info = {
        'Name': 'Tal',
        'GitHub': 'talshlmaovich@github.com',
        'Hobbies': ['Gaming', 'Coding'],
        'Gender': 'M'
    }

    context = {**user_info}    

    return render(request, 'profile_user.html', context)