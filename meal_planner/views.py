from django.shortcuts import render

def home(request):
    return render(request, 'meal_planner/index.html', {})
