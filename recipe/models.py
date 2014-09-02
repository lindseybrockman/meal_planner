from django.db import models


class Measurement(models.Model):
    """
    Measurments for various ingredients
    """
    MEASUREMENT_CHOICES = (('cups', 'cups'), ('tsp', 'tsp'), ('tbsp', 'tbsp'), ('entire', 'entire'), ('half', 'half'), ('quarter', 'quarter'), )
    amount = models.DecimalField(required=False)
    measurement = models.ChoiceField(required=False, choices=MEASUREMENT_CHOICES)


class Ingredient(models.Model):
    """
    ingredient model
    """
    name = models.CharField()
    approximated_cost = models.DecimalField(required=False, decimal_places=2, help_text="in USD")

class Recipe(models.Model):
    """
    recipe model
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title = models.CharField()
    prep_time = models.IntegerField(default=0, help_text='in minutes')
    cook_time = models.IntegerField(default=0, help_text='in minutes')
    instructions = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
