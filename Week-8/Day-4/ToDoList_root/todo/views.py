from django.shortcuts import render
from django.http import HttpResponse # pass view information into the browser
from .models import Todo, Category
from .forms import TodoForm


# Create your views here.

def todo (request):

    if request.method == 'POST':
        form_filled = TodoForm(request.POST)

        if form_filled.is_valid():
            title =  form_filled.cleaned_data['title']
            details = form_filled.cleaned_data['details']
            deadline_date = form_filled.cleaned_data['deadline_date']
            category = form_filled.cleaned_data['category']

            Todo.objects.create(
            title=title,
            details=details,
            deadline_date = deadline_date,
            category=category)
            

    context = {'form': TodoForm}
    return render(request, 'todo.html', context)



def display (request):

    all_todos = Todo.objects.order_by('date_creation')
    context = {'todos': all_todos}
    return render(request, 'display.html', context)
