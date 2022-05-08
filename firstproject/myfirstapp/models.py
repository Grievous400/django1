from django.db import models

# Create your models here.
class marque(models.Model):
    nom_marque = models.CharField(max_length=100)
    createur = models.CharField(max_length = 100)
    date_creation = models.DateField(blank=True, null = True)

    def __str__(self):
        chaine = f"{self.nom_marque}␣a été crée par␣{self.createur}␣en  {self.date_creation}"
        return chaine
    def dico(self):
        return {"nom_marque":self.nom_marque,"createur":self.createur,"date_creation":self.date_creation}

class voiture(models.Model):
    nom = models.CharField(max_length=100)
    modele =models.CharField(max_length=100)
    marque_voiture = models.CharField(max_length=100)
    date_constrution =models.DateField(blank=True, null = True)
    caracteristique =models.CharField(max_length = 100)

    def __str__(self):

        chaine2 = f"{self.nom} est le modèle {self.modele} construit en {self.date_constrution}.ces caractéritique sont {self.caracteristique}"
        return chaine2

    def dico(self):
        return {"nom":self.nom,"modele":self.modele,"marque_voiture":self.marque_voiture,"date_constrution":self.date_constrution,"caracteristique":self.caracteristique}