from django import forms
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory

from recipe.models import MeasuredIngredient, Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['created', 'modified']

    author = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())

IngredientFormset = inlineformset_factory(Recipe, MeasuredIngredient)

