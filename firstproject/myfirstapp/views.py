from django.shortcuts import render ,HttpResponseRedirect
from .forms import marqueForm
from .forms import voitureForm
from . import models
# Create your views here.
def index(request):
    liste=list(models.voiture.objects.all())
    liste2 = list(models.marque.objects.all())
    return render(request, 'myfirstapp/index.html',{"liste":liste,"liste2":liste2})

def formulaire1(request):
    if request.method =="POST":
        form = voitureForm(request)
        return render(request, "myfirstapp/formulaire1.html", {"form": form})
    else:
        form = voitureForm()
        return render(request, "myfirstapp/formulaire1.html", {"form": form})

def recup1(request):
    vform=voitureForm(request.POST)
    if vform.is_valid():
        voiture=vform.save()
        return HttpResponseRedirect("/myfirstapp")
    else:
        return render(request, "myfirstapp/formulaire1.html")


def formulaire2(request):
    if request.method =="POST":
        form = marqueForm(request)
        return render(request, "myfirstapp/formulaire2.html", {"form": form})
    else:
        form = marqueForm()
        return render(request,"myfirstapp/formulaire2.html", {"form": form})

def recup2(request):
    mform = marqueForm(request.POST)
    if mform.is_valid():
        marque = mform.save()
        return HttpResponseRedirect("myfirstapp")
    else:
        return render(request, "myfirstapp/formulaire2.html")
def affiche(request,id):
    voiture = models.voiture.objects.get(pk= id)

    return render(request,"myfirstapp/affiche.html",{"voiture":voiture})

def affiche2(request, id):
    marque = models.marque.objects.get(pk=id)

    return render(request, "myfirstapp/affiche2.html", { "marque": marque})

def update(request,id):
    voiture = models.voiture.objects.get(pk=id)
    form = voitureForm(voiture.dico())
    return render(request,"myfirstapp/formulaire1.html",{"form":form,"id":id})


def updatetraitement(request,id):
    vform = voitureForm(request.POST)
    if vform.is_valid():
        voiture = vform.save(commit=False)
        voiture.id = id
        voiture.save()
        return HttpResponseRedirect("/myfirstapp")
    else:
        return render(request, "myfirstapp/formulaire1.html",{"form":vform,"id":id})

def update2(request,id):
    marque = models.marque.objects.get(pk=id)
    form = marqueForm(marque.dico())
    return render(request,"myfirstapp/formulaire2.html",{"form":form,"id":id})


def updatetraitement2(request,id):
    mform = marqueForm(request.POST)
    if mform.is_valid():
        marque = mform.save(commit=False)
        marque.id = id
        marque.save()
        return HttpResponseRedirect("/myfirstapp")
    else:
        return render(request, "myfirstapp/formulaire2.html",{"form":mform,"id":id})

def delete1(request,id):
    voiture = models.voiture.objects.get(pk=id)
    voiture.delete()
    return HttpResponseRedirect("/myfirstapp")

def delete2(request,id):
    marque = models.marque.objects.get(pk=id)
    marque.delete()
    return HttpResponseRedirect("/myfirstapp")