from django import forms
from .models import Ingredient, Recipe
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

User = get_user_model()

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('title', 'measurement_unit', 'total_weight', 'cost')
        labels = {
            'title': 'Название',
            'measurement_unit': 'Единица измерения',
            'total_weight': 'Общий вес в граммах',
            'cost': 'Цена'
        }
        help_texts = {
            'total_weight': 'Введите общий вес в граммах.',
            'cost': 'Введите цену в рублях.'
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите название ингредиента'}),
            'total_weight': forms.NumberInput(attrs={'placeholder': 'Введите вес'}),
            'cost': forms.NumberInput(attrs={'placeholder': 'Введите цену'}),
        }


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'ingredients', 'author')
        labels = {
            'title': 'Название',
            'ingredients': 'Ингредиенты',
            'author': 'Автор рецепта'
        }
        help_texts = {
            'title': 'Введите название рецепта.',
            'ingredients': 'Выберите ингредиенты для рецепта.',
            'author': 'Выберите автора рецепта.'
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите название рецепта'}),
            'ingredients': forms.CheckboxSelectMultiple(),
            'author': forms.Select()
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')