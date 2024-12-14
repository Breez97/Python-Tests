from django.urls import path
from django.contrib.auth import views
from .views import (
    about,
    index,
    recipe,
    recipes,
    recipe_add,
    recipe_edit,
    recipe_delete,
    recipe_detail,
    ingredient,
    ingredients,
    ingredient_edit,
    ingredient_delete,
    user_logout,
    register,
    ingredient_add,
)

app_name = 'recipe_catalog'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('ingredient/', ingredient, name='ingredient'),
    path('ingredient/add/', ingredient_add, name='ingredient_add'),
    path('ingredient/edit/<int:pk>/', ingredient_edit, name='ingredient_edit'),
    path('ingredients/', ingredients, name='ingredients'),
    path('ingredient/delete/<int:pk>/', ingredient_delete, name='ingredient_delete'),
    path('recipes/', recipes, name='recipe'),
    path('recipe/add/', recipe_add, name='recipe_add'),
    path('recipe/edit/<int:pk>/', recipe_edit, name='recipe_edit'),
    path('recipe/delete/<int:pk>', recipe_delete, name='recipe_delete'),
    path('login/', views.LoginView.as_view(template_name='recipe_catalog/login.html'), name='login'),
    path('auth/logout/', user_logout, name='logout'),
    path('auth/register/', register, name='register'),
]
