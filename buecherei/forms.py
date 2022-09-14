from django.forms import ModelForm
from .models import Bibliotheksbenutzer, Autor, Verlag, Buch, Ausleihe


class BibliotheksbenutzerForm(ModelForm):
    class Meta:
        model = Bibliotheksbenutzer
        fields = ['name', 'nachname', 'strasse', 'plz']

    def __init__(self, *args, **kwargs):
        super(BibliotheksbenutzerForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'control nutzer'

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ['vorname', 'nachname']

    def __init__(self, *args, **kwargs):
        super(AutorForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'control autor'

class VerlagForm(ModelForm):
    class Meta:
        model = Verlag
        fields = ['name', 'telefonnummer', 'strasse', 'plz', 'ort']

    def __init__(self, *args, **kwargs):
        super(VerlagForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'control verlag'

class BuchForm(ModelForm):
    class Meta:
        model = Buch
        fields = ['isbn', 'verlag', 'titel', 'genre', 'jahr', 'autor']

    def __init__(self, *args, **kwargs):
        super(BuchForm, self).__init__(*args, **kwargs)
        self.fields['isbn'].widget.attrs['class'] = 'control isbn'
        self.fields['verlag'].widget.attrs['class'] = 'select verlag'
        self.fields['titel'].widget.attrs['class'] = 'control titel'
        self.fields['genre'].widget.attrs['class'] = 'control genre'
        self.fields['jahr'].widget.attrs['class'] = 'control jahr'
        self.fields["autor"].widget.attrs['class'] = 'multiple'

class AusleiheForm(ModelForm):
    class Meta:
        model = Ausleihe
        fields = ['buchID', 'bibliotheksbenutzerID', 'frist',]

    def __init__(self, *args, **kwargs):
        super(AusleiheForm, self).__init__(*args, **kwargs)
        self.fields['buchID'].queryset = Buch.objects.filter(ausgeliehen=False)
        self.fields["buchID"].widget.attrs['class'] = 'select ausleihe'
        self.fields["bibliotheksbenutzerID"].widget.attrs['class'] = 'select ausleihe'
        self.fields["frist"].widget.attrs['class'] = 'input ausleihe'
        self.fields["frist"].label = "Frist (in Tagen)"
        # for visible in self.visible_fields():
        #     visible.field.widget.attrs['class'] = 'control ausleihe'