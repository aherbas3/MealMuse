from django.db import models
from django.contrib.auth.models import User #using django's built in user model to link recipes and grocery lists to users

# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image_url = models.URLField(blank=True)
    instructions = models.TextField(blank=True)
    source_url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=255)
    amount = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=50, blank=True)      # e.g., grams, tbsp, cups
    category = models.CharField(max_length=100, blank=True) # e.g., produce, dairy, spices

    def __str__(self):
        return self.name

class GroceryList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.name