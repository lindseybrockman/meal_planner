from django.contrib import admin

from recipe.models import Ingredient, Measurement, Recipe

admin.site.register(Ingredient)
admin.site.register(Measurement)
admin.site.register(Recipe)
