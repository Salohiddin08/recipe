from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import View
from django.contrib.auth.hashers import make_password
from .models import User

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        image = request.FILES.get('image')

        if username and email and password:
            user = User(
                username=username,
                email=email,
                password=make_password(password),
                image=image
            )
            user.save()
            login(request, user)
            return redirect('home')  # 'home' sahifaga yo'naltirishi
        return render(request, 'register.html', {'error': 'Please provide all required fields.'})



class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        return render(request, 'login.html', {'error': 'Invalid credentials'})

