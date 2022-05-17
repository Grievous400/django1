from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class marqueForm(ModelForm):
    class Meta:
        model = models.marque
        fields = ('nom_marque', 'createur', 'date_creation')
        labels = {
            'marque' : _('Nom de la marque '),
            'createur' : _('createur ') ,
            'date_creation' : _('date de constrution  '),

        }
class voitureForm(ModelForm):
    class Meta:
        model =models.voiture
        fields =('nom','modele','marque','date_constrution','caracteristique')
        labels ={
            'nom': _('Nom de la voiture  '),
            'modele': _('Modèle de la voiture '),
            'marque':('Marque de la voiture'),
            'date_constrution' : _('Date de constrution '),
            'caracteristique' : _('Les caractéristiques '),
        }