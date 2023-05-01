from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, People

# Create your views here.

def home(request):
    obj = Place.objects.all()
    obj2 = People.objects.all()
    return render(request, "index.html", {'result': obj, 'people': obj2})


