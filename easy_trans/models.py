from django.contrib.gis.db import models
class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=255)
    # Ajoutez d'autres champs selon les besoins

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Destination(models.Model):
    nom_destination = models.CharField(max_length=100)
    coordonnees_geographiques = models.PointField()
    # Ajoutez d'autres champs selon les besoins

    def __str__(self):
        return self.nom_destination

class AgenceVoyage(models.Model):
    nom_agence = models.CharField(max_length=100)
    emplacement = models.PointField()
    classe_voyage = models.CharField(max_length=20)
    tarifs = models.DecimalField(max_digits=10, decimal_places=2)
    # Ajoutez d'autres champs selon les besoins

    def __str__(self):
        return self.nom_agence

class Restaurant(models.Model):
    nom_restaurant = models.CharField(max_length=100)
    emplacement = models.PointField()
    type_cuisine = models.CharField(max_length=50)
    menu = models.TextField()
    tarifs = models.DecimalField(max_digits=10, decimal_places=2)
    # Ajoutez d'autres champs selon les besoins

    def __str__(self):
        return self.nom_restaurant

class Hotel(models.Model):
    nom_hotel = models.CharField(max_length=100)
    emplacement = models.PointField()
    categorie_etoiles = models.IntegerField()
    tarifs_chambres = models.DecimalField(max_digits=10, decimal_places=2)
    # Ajoutez d'autres champs selon les besoins

    def __str__(self):
        return self.nom_hotel
