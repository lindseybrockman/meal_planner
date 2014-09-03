from django.forms import ModelForm
from recipe.models import Recipe

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        exclude = ['created', 'modified', 'chef']
