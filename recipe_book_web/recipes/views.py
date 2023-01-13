import re
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from recipes.models import Ingredient, Recipe
from django.views.generic import ListView
from recipes.forms import IngredientForm


# Create your views here.
class HomeListView(ListView):
    """Renders the home page, with a list of all recipes."""
    model = Recipe
    
    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context


def home(request):
    return render(request, "recipes/home.html")

def hello(request, name):
    return render(
        request,
        'recipes/hello.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def about(request):
    return render(request, "recipes/about.html")

def contact(request):
    return render(request, "recipes/contact.html")

def enter_ingredient(request):
    form = IngredientForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.save()
            return redirect("home")
        else:
            return render(request, "recipes/enter_ingredient.html", {"form": form})