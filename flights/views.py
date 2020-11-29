from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.

def index(request):
    context ={
        "flights": Flight.objects.all()
    }
    return render(request, "flights/index.html", context)

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk = flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not Exist!")
    context = {
        "flight": flight,
        "passenger": flight.passengers.all()
    }
    return render(request, "flights/flight.html", context)

