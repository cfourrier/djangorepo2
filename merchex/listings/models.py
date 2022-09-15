from django.db import models

# listings/models.py
class Band(models.Model):
    def __str__(self):
        return f'{self.name}'
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)


class Ad(models.Model):
    title = models.fields.CharField(max_length=100)

class Product(models.Model):
    class Type(models.TextChoices):
        RECORDS = 'records'
        CLOTHING = 'clothings'
        MISCELLANEOUS = 'miscellaneous'
    description = models.fields.CharField(max_length=100)
    sold = models.fields.BooleanField(default=False)
    type = models.fields.CharField(choices=Type.choices, max_length=30)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

