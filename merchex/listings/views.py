# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Ad

def band_list(request):  # renommer la fonction de vue
   bands = Band.objects.all()
   return render(request,
           'listings/band_list.html',  # pointe vers le nouveau nom de modèle
           {'bands': bands})

def band_detail(request, id):
  band = Band.objects.get(id=id)  # nous insérons cette ligne pour obtenir le Band avec cet id
  return render(request,
          'listings/band_detail.html',
          {'band': band}) # nous mettons à jour cette ligne pour passer le groupe au gabarit

def about(request):
    bands = Band.objects.all()
    return render(request,
    'listings/about-us.html',
    {'bands': bands})

def contact(request):
    bands = Band.objects.all()
    return render(request,
    'listings/contact.html',
    {'bands': bands})

def listings(request):
    ads = Ad.objects.all()
    return render(request,
    'listings/listings.html',
    {'ads': ads})
    #return HttpResponse(f"""
    #    <h2>{ads[0].title}</h2>
    #    <h2>{ads[1].title}</h2>
    #    <h2>{ads[2].title}</h2>
    #    <h2>{ads[3].title}</h2>
#""")