# ~/projects/django-web-app/merchex/listings/views.py
from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Product
from listings.models import Ad
from listings.forms import ContactUsForm


def band_list(request):  # renommer la fonction de vue
   bands = Band.objects.all()
   return render(request,
           'listings/band_list.html',  # pointe vers le nouveau nom de modèle
           {'bands': bands})

def band_detail(request, id):
  band = Band.objects.get(id=id)
  return render(request,
          'listings/band_detail.html',
          {'band': band})

def product_list(request):
    products = Product.objects.all()
    return render(request,
    'listings/product_list.html',
    {'products': products})

def product_detail(request, id):
  product = Product.objects.get(id=id)
  return render(request,
          'listings/product_detail.html',
          {'product': product})

def about(request):
    bands = Band.objects.all()
    return render(request,
    'listings/about-us.html',
    {'bands': bands})

def contact(request):
  form = ContactUsForm()  # ajout d’un nouveau formulaire ici
  return render(request,
          'listings/contact.html',
          {'form': form})  # passe ce formulaire au gabarit