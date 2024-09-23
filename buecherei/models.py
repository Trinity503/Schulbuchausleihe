from django.db import models

# Create your models here.

class Bibliotheksbenutzer(models.Model):
    name = models.CharField(max_length=64)
    nachname = models.CharField(max_length=64)
    strasse = models.CharField(max_length=64)
    plz = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.nachname}"

    class Meta:
        verbose_name_plural = "Bibliotheksbenutzer"

class Autor(models.Model):
    vorname = models.CharField(max_length=64)
    nachname = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.vorname} {self.nachname}"

    class Meta:
        verbose_name_plural = "Autoren"

class Verlag(models.Model):
    name = models.CharField(max_length=64)
    telefonnummer = models.CharField(max_length=64)
    strasse = models.CharField(max_length=64)
    plz = models.IntegerField()
    ort = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Verlage"


class Buch(models.Model):
    isbn = models.IntegerField()
    verlag = models.ForeignKey(Verlag, on_delete=models.CASCADE, related_name="verlag")
    titel = models.CharField(max_length=64)
    genre = models.CharField(max_length=64)
    jahr = models.IntegerField()
    autor = models.ManyToManyField(Autor)
    ausgeliehen = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.titel}"

    class Meta:
        verbose_name_plural = "Bücher"


class Ausleihe(models.Model):
    buchID = models.ForeignKey(Buch,on_delete=models.CASCADE)
    bibliotheksbenutzerID = models.ForeignKey(Bibliotheksbenutzer, on_delete=models.CASCADE)
    frist = models.IntegerField(default="30", verbose_name="Penis", null=True)
    verbleibend = models.IntegerField(null=True)
    ausleihdatum = models.DateField(auto_now_add=True)
    rueckgabedatum = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.buchID} {self.bibliotheksbenutzerID} {self.ausleihdatum} {self.rueckgabedatum}"

    class Meta:
        verbose_name_plural = "Ausleihe"

