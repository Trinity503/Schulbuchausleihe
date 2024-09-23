"""Buecherei_SRH_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from buecherei import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('nutzer/', views.nutzer, name='nutzer'),
    path('buch/', views.buch, name='buch'),
    path('ausleih/', views.ausleih, name='ausleih'),
    path('add_autor/', views.add_autor, name='add_autor'),
    path('add_buch/', views.add_buch, name='add_buch'),
    path('add_buch_isbn/', views.add_buch, name='add_buch_isbn'),
    path('add_nutzer/', views.add_nutzer, name='add_nutzer'),
    path('add_verlag/', views.add_verlag, name='add_verlag'),
    path('verlag/<int:id>/', views.verlag_detail, name='verlag'),
    path('autor/<int:id>/', views.autor_detail, name='autor_detail'),
    path('buch/<int:id>/', views.buch_detail, name='buch_detail'),
    path('nutzer/<int:id>/', views.nutzer_detail, name='nutzer_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
