from django.urls import path
from .views import Login, RegisterView
app_name = 'users'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
