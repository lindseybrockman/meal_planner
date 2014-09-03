from django.contrib import admin

from recipe.models import Ingredient, MeasuredIngredient, Recipe

admin.site.register(Ingredient)
admin.site.register(MeasuredIngredient)
admin.site.register(Recipe)
