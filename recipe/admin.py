from django.contrib import admin
from .models import Recipe, RecipeText, Ingredient, Contact, CommentRecipe

admin.site.register([Recipe, RecipeText, Ingredient, Contact, CommentRecipe])
