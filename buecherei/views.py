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

def add_autor(request):
    form = AutorForm(request.POST or None)
    return render(request, 'add_autor.html', {'form': AutorForm()})

def add_buch(request):
    form = BuchForm(request.POST or None)
    return render(request, 'add_buch.html', {'form': BuchForm()})

def add_nutzer(request):
    form = BibliotheksbenutzerForm(request.POST or None)
    return render(request, 'add_nutzer.html', {'form': BibliotheksbenutzerForm()})

def add_verlag(request):
    form = VerlagForm(request.POST or None)
    return render(request, 'add_verlag.html', {'form': VerlagForm()})