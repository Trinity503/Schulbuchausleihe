from django.forms import ModelForm
from .models import Bibliotheksbenutzer, Autor, Verlag, Buch, Ausleihe
from bootstrap_modal_forms.forms import BSModalModelForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class BibliotheksbenutzerForm(PopRequestMixin, CreateUpdateAjaxMixin, ModelForm):
    class Meta:
        model = Bibliotheksbenutzer
        fields = ['name', 'nachname', 'strasse', 'plz']

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ['vorname', 'nachname']

class VerlagForm(ModelForm):
    class Meta:
        model = Verlag
        fields = ['name', 'telefonnummer', 'strasse', 'plz', 'ort']

class BuchForm(ModelForm):
    class Meta:
        model = Buch
        fields = ['isbn', 'verlag', 'titel', 'genre', 'jahr']

class AusleiheForm(ModelForm):
    class Meta:
        model = Ausleihe
        fields = ['buchID', 'bibliotheksbenutzerID', 'rueckgabedatum']