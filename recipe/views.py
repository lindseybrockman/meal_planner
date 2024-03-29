from django.shortcuts import render

from chef.models import Chef
from recipe.forms import IngredientFormset, RecipeForm

def add(request):
    recipe_form = RecipeForm(request.POST or None)
    ingredient_formset = IngredientFormset(request.POST or None, prefix='ingredient')
    if request.method == 'POST':
        recipe_form.fields['chef'] = Chef.get_chef(request.user)
        if recipe_form.is_valid() and ingredient_formset.is_valid():
            recipe_form.save()
            ingredient_formset.save()

    context = {
        'recipe_form': recipe_form,
        'ingredient_formset': ingredient_formset,
    }
    return render(request, 'recipe/add.html', context)
