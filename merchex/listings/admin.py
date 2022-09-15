# listings/admin.py

from django.contrib import admin

from listings.models import Band
#from bands.models import Band
from listings.models import Ad
from listings.models import Product


#admin.site.register(Band)

class BandAdmin(admin.ModelAdmin): 
    list_display = ('name', 'genre') # liste les champs que nous voulons sur l'affichage de la liste

class ProductAdmin(admin.ModelAdmin): 
    list_display = ('description', 'type', 'sold')

admin.site.register(Band, BandAdmin)
admin.site.register(Ad)
admin.site.register(Product, ProductAdmin)