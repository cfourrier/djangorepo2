# listings/admin.py

from django.contrib import admin

from listings.models import Band
#from bands.models import Band
from listings.models import Ad
from listings.models import Productos


#admin.site.register(Band)

class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'genre') # liste les champs que nous voulons sur l'affichage de la liste

class ProductoAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('description', 'type', 'sold') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Band, BandAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument
admin.site.register(Ad)
admin.site.register(Productos, ProductoAdmin)