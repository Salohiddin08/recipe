from django.shortcuts import render, redirect
from django.views import View
from .models import Recipe, Contact, CommentRecipe
import requests
from django.urls import reverse

class Home(View):
    def get(self, request):
        recipes = Recipe.objects.all()
        # two_recipes = Recipe.objects.all().order_by('-created_at')
        two_recipes = Recipe.objects.all().order_by()[:2]
        context = {'recipes': recipes, 'two_recipes': two_recipes}
        return render(request, 'index.html', context=context)


class About(View):
    def get(self, request):
        return render(request, 'about.html')
    

class Blog(View):
    def get(self, request):
        return render(request, 'blog-post.html')
    

class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        ism = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(name=ism, email=email, subject=subject, message=message)
        self.send_telegram_message(name=ism, email=email, subject=subject, message=message)
        return render(request, 'index.html')

    def send_telegram_message(self, name, email, subject, message):
        bot_token = '7006912627:AAED3MVWrg_GWUMr1D5da2U2s8WD14lhTnM'
        chat_id = 816660001
        telegram_api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        xabar = (f'Yangi xabar keldi\n'
                 f'Name: {name}\n'
                 f'Email: {email}\n'
                 f'Subject: {subject}\n'
                 f'Message: {message}')

        payload = {
            'chat_id': chat_id,
            'text': xabar
        }
        response = requests.post(url=telegram_api_url, data=payload)
        if response.status_code != 200:
            print(f"Failed to send message to Telegram. Status code: {response.status_code}, Response: {response.text}")


class RecipePost(View):
    def get(self, request):
        return render(request, 'receipe-post.html')
    

class Element(View):
    def get(self, request):
        return render(request, 'elements.html')


class RecipeDetail(View):
    def get(self, request, recipe_id):
        recipe = Recipe.objects.get(id=recipe_id)
        return render(request, 'receipe-post.html', context={'recipe': recipe})

    def post(self, request, recipe_id):
        recipe = Recipe.objects.get(id=recipe_id)
        user = request.user
        message = request.POST.get('message')
        print(message, user, recipe)
        CommentRecipe.objects.create(user=user, recipe=recipe, text=message)
        return redirect(reverse('recipe:recipe-detail', kwargs={'id': recipe_id}))
