from django.shortcuts import render
from .models import Person


# Create your views here.
def index(request):
    person = Person.objects.all()
    return render(request, 'index.html', {'person': person})