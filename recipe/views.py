from django.shortcuts import render

from recipe forms import RecipeForm

def recipe_add(request):
    form = RecipeForm(request.get('POST'))
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    
    context = {'form': form}
    render(request, 'recipe/add.html', context)
