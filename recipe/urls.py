from django.urls import path
from .import views

app_name = 'recipe'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('recipe-post/', views.RecipePost.as_view(), name='recipe_post'),
    path('elements/', views.Element.as_view(), name='elements'),
    path('blog/', views.Blog.as_view(), name='blog'),
    path('recipe-detail/<int:recipe_id>/', views.RecipeDetail.as_view(), name='recipe-detail'),

]
