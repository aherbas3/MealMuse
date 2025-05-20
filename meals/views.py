from django.shortcuts import render
from django.http import HttpResponse
from .models import GroceryList, Recipe, Ingredient

# Create your views here.
def index(response, id):
    g = GroceryList.objects.get(id = id)
    r = g.recipes.get(id=1) #just get the first item tbh since we have just 1 rn
    return HttpResponse("<h1>%s</h2><br></br><p>%s</p>" %(g.name, r.title))