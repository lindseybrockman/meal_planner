from django.contrib.auth.models import User
from django.db import models

class Ingredient(models.Model):
    """
    ingredient model
    """
    name = models.CharField(max_length=200)
    approximated_cost = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=10, help_text="in USD")

    def __unicode__(self):
        return self.name


class Recipe(models.Model):
    """
    recipe model
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    prep_time = models.IntegerField(default=0, help_text='in minutes')
    cook_time = models.IntegerField(default=0, help_text='in minutes')
    instructions = models.TextField()
    author = models.ForeignKey(User)

    def __unicode__(self):
        return "{} (by {})".format(self.title, self.chef.username)


class MeasuredIngredient(models.Model):
    """
    Measurments for various ingredients
    """
    MEASUREMENT_CHOICES = (
            ('cups', 'cups'),
            ('tsp', 'tsp'),
            ('tbsp', 'tbsp'),
            ('entire', 'entire'),
            ('half', 'half'),
            ('quarter', 'quarter'),
        )
    amount = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=10)
    measurement = models.CharField(blank=True, null=True, max_length=20, choices=MEASUREMENT_CHOICES)
    ingredient = models.ForeignKey(Ingredient)
    recipe = models.ForeignKey(Recipe)

    def __unicode__(self):
        return "{} {} {}".format(self.amount, self.measurement, self.ingredient.name)



