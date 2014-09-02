from django.db import models

from recipe.models import Ingredient

class Pantry(models.Model):
    ingredients = models.ManyToManyField(Ingredient) 
