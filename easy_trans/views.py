from django.shortcuts import render
from django.http import HttpResponse
from .models import Utilisateur, Destination, AgenceVoyage, Restaurant, Hotel

def lister_utilisateurs(request):
    utilisateurs = Utilisateur.objects.all()
    context = {'utilisateurs': utilisateurs}
    return render(request, 'lister_utilisateurs.html', context)

def lister_destinations(request):
    destinations = Destination.objects.all()
    context = {'destinations': destinations}
    return render(request, 'lister_destinations.html', context)

def lister_agences_voyage(request):
    agences_voyage = AgenceVoyage.objects.all()
    context = {'agences_voyage': agences_voyage}
    return render(request, 'lister_agences_voyage.html', context)

def lister_restaurants(request):
    restaurants = Restaurant.objects.all()
    context = {'restaurants': restaurants}
    return render(request, 'lister_restaurants.html', context)

def lister_hotels(request):
    hotels = Hotel.objects.all()
    context = {'hotels': hotels}
    return render(request, 'lister_hotels.html', context)
