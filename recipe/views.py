from django.shortcuts import render

from recipe.forms import RecipeForm

def add(request):
    form = RecipeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    
    context = {'form': form}
    return render(request, 'recipe/add.html', context)
