from django.db import models

# Create your models here.
class marque(models.Model):
    nom_marque = models.CharField(max_length=100)
    createur = models.CharField(max_length = 100)
    date_creation = models.DateField(blank=True, null = True)

    def __str__(self):
        chaine = f"{self.nom_marque}␣a été crée par␣{self.createur}␣en  {self.date_creation}"
        return chaine

class voiture(models.Model):
    nom = models.CharField(max_length=100)
    modele =models.CharField(max_length=100)
    marque_voiture = models.CharField(max_length=100)
    date_constrution =models.DateField(blank=True, null = True)
    caracteristique =models.CharField(max_length = 100)

    def __str__(self):

        chaine2 = f"{self.nom} est le modèle {self.modele} construit en {self.date_constrution}.c'est caractéritique sont {self.caracteristique}"
        return chaine2
