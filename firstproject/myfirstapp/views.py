from django.shortcuts import render
from .forms import marqueForm
from .forms import voitureForm
# Create your views here.
def index(request):
    return render(request, 'myfirstapp/index.html')

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

        return render(request, "myfirstapp/recup1.html")
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
        return render(request, "myfirstapp/recup2.html")
    else:
        return render(request, "myfirstapp/formulaire2.html")