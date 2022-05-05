from django.db import models

# Create your models here.
class marque(models.Model):
    nom_marque = models.CharField(max_length=100)
    createur = models.CharField(max_length = 100)
    date_creation = models.DateField(blank=True, null = True)

class voiture(models.Model):
    nom = models.CharField(max_length=100)
    modele =models.CharField(max_length=100)
    date_constrution =models.DateField(blank=True, null = True)
    caracteristique =models.CharField(max_length = 100)

def __str__(self):
    chaine = f"{self.nom_marque}␣écrit␣par␣{self.createur}␣édité le  {self.date_creation}"
    chaine2 = f"{self.nom} est le modèle {self.modele} construit en {self.date_constrution}.c'est caractéritique sont {self.carateristique}"
    return chaine ,chaine2
