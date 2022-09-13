from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from .forms import BibliotheksbenutzerForm, AutorForm, VerlagForm, BuchForm, AusleiheForm
from .models import Bibliotheksbenutzer, Autor, Verlag, Buch, Ausleihe
from datetime import datetime, date
from django.contrib import messages
from bootstrap_modal_forms.mixins import PassRequestMixin

# Create your views here.

def index(request):
    if request.method == 'POST':
        delete_id = request.POST.get("delete")
        if delete_id:
            ausleihe = Ausleihe.objects.get(id=delete_id)
            ausleihe.delete()
            messages.info(request, 'Der Eintrag wurde erfolgreich gelöscht!', extra_tags='message is-success')
            return redirect(reverse('index'))
        rueckgabe_id = request.POST.get("rueckgabe")
        if rueckgabe_id and not Ausleihe.objects.get(id=rueckgabe_id).rueckgabedatum:
            rueckgabe = Ausleihe.objects.get(id=rueckgabe_id)
            Buch.objects.filter(id=rueckgabe.buchID.id).update(ausgeliehen=False)
            rueckgabe.rueckgabedatum = date.today()
            rueckgabe.frist = '--'
            rueckgabe.save()
            messages.info(request, 'Das Buch wurde erfolgreich zurückgegeben!', extra_tags='message is-success')
            return redirect(reverse('index'))
        else:
            messages.info(request, 'Das Buch wurde bereits zurückgegeben!', extra_tags='message is-warning')
    alle_ausleihe = Ausleihe.objects.all()
    paginator = Paginator(alle_ausleihe, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {
        "page_obj": page_obj,
    })

def nutzer(request):
    if request.method == 'POST' and request.POST.get("delete"):
        id = request.POST.get("delete")
        nutzer = Bibliotheksbenutzer.objects.get(id=id)
        nutzer.delete()
        messages.info(request, 'Der Nutzer wurde erfolgreich gelöscht!', extra_tags='message is-success')
        return redirect(reverse('nutzer'))
    if request.method == 'POST' and request.POST.get("edit"):
        id = request.POST.get("edit")
        form = BibliotheksbenutzerForm(instance=Bibliotheksbenutzer.objects.get(id=id))
        return render(request, 'edit.html', {
                        'id': id,
                        'form': form,
                        })
    if request.method == 'POST' and request.POST.get("update"):
        form = BibliotheksbenutzerForm(request.POST or None)
        if form.is_valid():
            nutzer = Bibliotheksbenutzer.objects.get(id=request.POST.get("update"))
            nutzer.name = form.cleaned_data['name']
            nutzer.nachname = form.cleaned_data['nachname']
            nutzer.strasse = form.cleaned_data['strasse']
            nutzer.plz = form.cleaned_data['plz']
            nutzer.save()
            messages.info(request, 'Der Nutzer wurde erfolgreich editiert!', extra_tags='message is-success')
            return redirect(reverse('nutzer'))
        else:
            messages.info(request, 'Ups, da fehlt noch was!', extra_tags='message is-danger')
        return render(request, 'edit.html', {
                        'form': form,
                        })
    alle_nutzer = Bibliotheksbenutzer.objects.all()
    paginator = Paginator(alle_nutzer, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'nutzer.html', {
        "page_obj": page_obj,
    })

def buch(request):
    if request.method == 'POST' and request.POST.get("delete"):
        id = request.POST.get("delete")
        buch = Buch.objects.get(id=id)
        buch.delete()
        messages.info(request, 'Das Buch wurde erfolgreich gelöscht!', extra_tags='message is-success')
        return redirect(reverse('buch'))
    if request.method == 'POST' and request.POST.get("edit"):
        form = BuchForm(instance=Buch.objects.get(id=request.POST.get("edit")))
        return render(request, 'edit.html', {
                        'id': request.POST.get("edit"),
                        'form': form,
                        })
    if request.method == 'POST' and request.POST.get("update"):
        form = BuchForm(request.POST or None)
        if form.is_valid():
            buch = Buch.objects.get(id=request.POST.get("update"))
            buch.isbn = form.cleaned_data['isbn']
            buch.titel = form.cleaned_data['titel']
            buch.verlag = form.cleaned_data['verlag']
            buch.genre = form.cleaned_data['genre']
            buch.jahr = form.cleaned_data['jahr']
            buch.save()
            messages.info(request, 'Das Buch wurde erfolgreich editiert!', extra_tags='message is-success')
            return redirect(reverse('buch'))
        else:
            messages.info(request, 'Ups, da fehlt noch was!', extra_tags='message is-danger')
        return render(request, 'edit.html', {
                        'form': form,
                        })
    buecher = Buch.objects.all()
    paginator = Paginator(buecher, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    autor = [Autor.objects.get(id=x.id) for x in page_obj.object_list]
    combo = zip(page_obj.object_list, autor)
    return render(request, 'buch.html', {
        "page_obj": page_obj,
        "combo": combo,
    })

def ausleih(request):
    form = AusleiheForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        verfuegbarkeit = Buch.objects.filter(ausgeliehen=False).get(id=form.cleaned_data['buchID'].id)
        if verfuegbarkeit:
            verfuegbarkeit.ausgeliehen = True
            verfuegbarkeit.save()
            form.save()
            messages.info(request, 'Das Buch wurde erfolgreich ausgeliehen!', extra_tags='message is-success')
            return redirect(reverse('index'))
        else:
            messages.info(request, 'Das Buch ist leider nicht verfügbar!', extra_tags='message is-warning')
    elif request.method == 'POST' and not form.is_valid():
        messages.info(request, 'Ups, da fehlt noch was!', extra_tags='message is-danger')
    return render(request, 'ausleih.html',
                    {'form': AusleiheForm()},
                    )

def add_autor(request):
    form = AutorForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.info(request, 'Der Autor wurde erfolgreich hinzugefügt!', extra_tags='message is-success')
        return redirect(reverse('index'))
    elif request.method == 'POST' and not form.is_valid():
        messages.info(request, 'Ups, da fehlt noch was!', extra_tags='message is-danger')
    return render(request, 'add.html', {'form': AutorForm()})

def add_buch(request):
    form = BuchForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.info(request, 'Das Buch wurde erfolgreich hinzugefügt!', extra_tags='message is-success')
        return redirect(reverse('buch'))
    elif request.method == 'POST' and not form.is_valid():
        messages.info(request, 'Ups, da fehlt noch was!', extra_tags='message is-danger')
    return render(request, 'add.html', {'form': BuchForm()})

def add_nutzer(request):
    form = BibliotheksbenutzerForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.info(request, 'Der Nutzer wurde erfolgreich hinzugefügt!', extra_tags='message is-success')
        return redirect(reverse('nutzer'))
    elif request.method == 'POST' and not form.is_valid():
        messages.info(request, 'Ups, da fehlt noch was!', extra_tags='message is-danger')
    return render(request, 'add.html', {'form': BibliotheksbenutzerForm()})

def add_verlag(request):
    form = VerlagForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.info(request, 'Der Verlag wurde erfolgreich hinzugefügt!', extra_tags='message is-success')
        return redirect(reverse('buch'))
    elif request.method == 'POST' and not form.is_valid():
        messages.info(request, 'Ups, da fehlt noch was!', extra_tags='message is-danger')
    return render(request, 'add.html', {'form': VerlagForm()})

def autor_detail(request, id):
    ansicht = "autor"
    autor = Autor.objects.get(id=id)
    buecher = Buch.objects.filter(autor=autor).order_by('titel')[:1]
    return render(request, 'detail_view.html', {
        'autor': autor,
        'buecher': buecher,
        'ansicht': ansicht,
    })

def buch_detail(request, id):
    ansicht = "buch"
    buch = Buch.objects.get(id=id)
    autor = Autor.objects.get(id=buch.autor.get().id)
    return render(request, 'detail_view.html', {
        'buch': buch,
        'autor': autor,
        'ansicht': ansicht,
    })

def nutzer_detail(request, id):
    nutzer = Bibliotheksbenutzer.objects.get(id=id)
    ansicht = "nutzer"
    buch = Ausleihe.objects.filter(bibliotheksbenutzerID=nutzer)
    frist = []
    for x in buch:
        if x.rueckgabedatum == None:
            remaining = (x.ausleihdatum - date.today()).days + x.frist
            frist.append(f"{remaining} Tage")
        else:
            frist.append("Rückgabe erfolgt!")
    buecher = zip(buch, frist)
    return render(request, 'detail_view.html', {
        "nutzer": nutzer,
        'ansicht': ansicht,
        'buecher': buecher,
    })
def verlag_detail(request, id):
    verlag = Verlag.objects.get(id=id)
    ansicht = "verlag"
    titel_len = set(Buch.objects.filter(verlag_id=verlag).values_list('titel', flat=True))
    buecher = Buch.objects.filter(verlag_id=verlag).values('id', 'titel')[:len(titel_len)]
    print(buecher)
    return render(request, 'detail_view.html', {
        'verlag': verlag,
        'buecher': buecher,
        'ansicht': ansicht,
    })