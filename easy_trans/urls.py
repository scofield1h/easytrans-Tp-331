# easytrans/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.lister_utilisateurs, name='accueil'),  # Rediriger vers la liste des utilisateurs
    path('utilisateurs/', views.lister_utilisateurs, name='lister_utilisateurs'),
    path('destinations/', views.lister_destinations, name='lister_destinations'),
    path('agences_voyage/', views.lister_agences_voyage, name='lister_agences_voyage'),
    path('restaurants/', views.lister_restaurants, name='lister_restaurants'),
    path('hotels/', views.lister_hotels, name='lister_hotels'),
    # Autres URLs de votre application
]

