# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Ad

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :<p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
""")

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def contact(request):
    return HttpResponse('<h1>Contact</h1> <p>Para información</p>')

def listings(request):
    ads = Ad.objects.all()
    return HttpResponse(f"""
        <h2>{ads[0].title}</h2>
        <h2>{ads[1].title}</h2>
        <h2>{ads[2].title}</h2>
        <h2>{ads[3].title}</h2>
""")