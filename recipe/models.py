from django.db import models
from django.utils import timezone
from users.models import User


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    star = models.IntegerField()
    image = models.ImageField(upload_to='recipe-images/')
    created_at = models.DateField(auto_now_add=True)
    prep = models.IntegerField()
    cook = models.IntegerField()
    yields = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class RecipeText(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='text')
    text = models.TextField()

    def __str__(self) -> str:
        return f'{self.recipe.name} star-> {self.recipe.star}'


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredient')

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class CommentRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    def __str__(self):
        return self.text[:50]


class MainPage(models.Model):
    pass


