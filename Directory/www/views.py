from django.shortcuts import render
from .models import Person


# Create your views here.
def index(request):
    person = Person.objects.all()
    return render(request, 'index.html', {'person': person})

def detail(request, slug):
    person = Person.objects.get(slug=slug)
    return render(request, 'detail.html', {'person': person})

def edit(request, slug):
    person = Person.objects.get(slug=slug)
    return render(request, 'detail.html', {'person': person})