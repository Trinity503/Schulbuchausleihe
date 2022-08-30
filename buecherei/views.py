from django.shortcuts import render, redirect, reverse
from .forms import BibliotheksbenutzerForm, AutorForm, VerlagForm, BuchForm, AusleiheForm
from .models import Bibliotheksbenutzer, Autor, Verlag, Buch, Ausleihe
from bootstrap_modal_forms.mixins import PassRequestMixin

# Create your views here.

def index(request):
    form = BibliotheksbenutzerForm(request.POST or None)
    return render(request, 'index.html', {'form': BibliotheksbenutzerForm()})

def nutzer(request):
    return render(request, 'nutzer.html', {
        "nutzer": Bibliotheksbenutzer.objects.all(),
    })

def buch(request):
    return render(request, 'buch.html', {
        "buecher": Buch.objects.all(),
    })

def ausleih(request):
    return render(request, 'ausleih.html')