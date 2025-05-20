from django.contrib import admin
from .models import GroceryList, Recipe, Ingredient

# Register your models here.
admin.site.register(GroceryList)
admin.site.register(Recipe)
admin.site.register(Ingredient)
