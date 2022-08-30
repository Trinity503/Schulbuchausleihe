from django.contrib import admin
from .models import Bibliotheksbenutzer, Autor, Verlag, Buch, Ausleihe
# Register your models here.

class BuchInline(admin.StackedInline):
    model = Buch.autor.through

class BibliotheksbenutzerAdmin(admin.ModelAdmin):
    list_display = ("name", "nachname", "strasse", "plz")
    list_display_links = ("name", "nachname")
    list_filter = ("name", "nachname")
    search_fields = ("name", "nachname")

class AutorAdmin(admin.ModelAdmin):
    inlines = [BuchInline]
    list_display = ("vorname", "nachname")
    list_display_links = ("vorname", "nachname")
    list_filter = ("vorname", "nachname")
    search_fields = ("vorname", "nachname")

class VerlagAdmin(admin.ModelAdmin):
    list_display = ("name", "telefonnummer", "strasse", "plz", "ort")
    list_display_links = ("name", "telefonnummer")
    list_filter = ("name", "telefonnummer")
    search_fields = ("name", "telefonnummer")

class BuchAdmin(admin.ModelAdmin):
    list_display = ("titel", "genre", "jahr", "verlag",)
    list_display_links = ("titel", "verlag")
    filter_horizontal = ("autor", )
    search_fields = ("titel", "verlag")

class AusleiheAdmin(admin.ModelAdmin):
    list_display = ("buchID", "bibliotheksbenutzerID", "ausleihdatum", "rueckgabedatum")
    list_display_links = ("buchID", "bibliotheksbenutzerID")
    raw_id_fields = ("buchID", "bibliotheksbenutzerID")
    list_filter = ("buchID", "bibliotheksbenutzerID")
    search_fields = ("buchID", "bibliotheksbenutzerID")

admin.site.register(Bibliotheksbenutzer, BibliotheksbenutzerAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Verlag, VerlagAdmin)
admin.site.register(Buch, BuchAdmin)
admin.site.register(Ausleihe, AusleiheAdmin)