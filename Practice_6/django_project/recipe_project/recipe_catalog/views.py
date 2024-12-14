from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .models import Recipe, Ingredient
from .forms import IngredientForm, RecipeForm, CustomUserCreationForm


def index(request):
    recipes = Recipe.objects.all()
    return render(
        request=request,
        template_name='recipe_catalog/index.html',
        context={'recipes': recipes}
    )


def about(request):
    return render(
        request=request,
        template_name='recipe_catalog/about.html'
    )


def recipe_detail(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
        recipes = Recipe.objects.all()
        is_author = request.user == recipe.author
    except Recipe.DoesNotExist:
        return render(
            request=request,
            template_name='recipe_catalog/recipe_not_found.html'
        )
    return render(
        request=request,
        template_name='recipe_catalog/recipe_detail.html',
        context={
            'recipe_id': recipe.id,
            'title': recipe.title,
            'ingredients': recipe.ingredients.order_by('title'),
            'sum_weight': recipe.ingredients.aggregate(total=Sum('total_weight'))['total'],
            'sum_cost': recipe.ingredients.aggregate(total=Sum('cost'))['total'],
            'recipes': recipes,
            'is_author': is_author,
        }
    )


@login_required
def ingredient(request):
    template = 'recipe_catalog/ingredient_form.html'
    form = IngredientForm(request.POST or None)
    if form.is_valid():
        ingredient = form.save(commit=False)
        ingredient.author = request.user
        ingredient.save()
        return redirect('recipe_catalog:ingredients')
    context = {'form': form}
    return render(request, template, context)


def ingredients(request):
    ingredient_list = Ingredient.objects.all()
    context = {'ingredients': ingredient_list}
    return render(request, 'recipe_catalog/ingredient_list.html', context)


@login_required
def ingredient_add(request):
    if not request.user.is_authenticated:
        raise PermissionDenied
    template = 'recipe_catalog/ingredient_add.html'
    form = IngredientForm(request.POST or None)
    if form.is_valid():
        ingredient = form.save(commit=False)
        ingredient.author = request.user
        ingredient.save()
        messages.success(request, 'Ингредиент был успешно добавлен')
        return redirect('recipe_catalog:ingredients')
    context = {'form': form}
    return render(request, template, context)


@login_required
def ingredient_edit(request, pk):
    instance = get_object_or_404(Ingredient, pk=pk)
    if request.user != instance.author:
        raise PermissionDenied("Вы не можете редактировать этот ингредиент")
    form = IngredientForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('recipe_catalog:ingredients')
    context = {'form': form}
    return render(request, 'recipe_catalog/ingredient_edit.html', context)


@login_required
def ingredient_delete(request, pk):
    instance = get_object_or_404(Ingredient, pk=pk)
    if request.user != instance.author:
        raise PermissionDenied("Вы не можете удалить этот ингредиент")
    if request.method == 'POST':
        instance.delete()
        return redirect('recipe_catalog:ingredients')
    context = {'ingredient': instance}
    return render(request, 'recipe_catalog/ingredient_confirm_delete.html', context)


@login_required
def recipe(request):
    template = 'recipe_catalog/recipe_form.html'
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        recipe = form.save(commit=False)
        recipe.author = request.user
        recipe.save()
        form.save_m2m()
        return redirect('recipe_catalog:index')
    context = {'form': form}
    return render(request, template, context)


def recipes(request):
    recipe_list = Recipe.objects.all()
    context = {'recipes': recipe_list}
    return render(request, 'recipe_catalog/index.html', context)


@login_required
def recipe_add(request):
    if not request.user.is_authenticated:
        raise PermissionDenied
    template = 'recipe_catalog/recipe_add.html'
    user_ingredients = Ingredient.objects.filter(author=request.user)
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            form.save_m2m()
            messages.success(request, 'Рецепт был успешно добавлен')
            return redirect('recipe_catalog:index')
    else:
        form = RecipeForm()
        form.base_fields['ingredients'].queryset = user_ingredients
    context = {
        'form': form,
        'user_ingredients': user_ingredients
    }
    return render(request, template, context)


@login_required
def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.user != recipe.author:
        raise PermissionDenied("Вы не можете редактировать этот рецепт")
    user_ingredients = Ingredient.objects.filter(author=request.user)
    form = RecipeForm(request.POST or None, request.FILES or None, instance=recipe)
    form.base_fields['ingredients'].queryset = user_ingredients
    if form.is_valid():
        updated_recipe = form.save()
        updated_recipe.ingredients.set(form.cleaned_data['ingredients'])
        return redirect('recipe_catalog:recipe_detail', pk=updated_recipe.pk)
    context = {
        'form': form, 
        'recipe': recipe,
        'user_ingredients': user_ingredients
    }
    return render(request, 'recipe_catalog/recipe_edit.html', context)


@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.user != recipe.author:
        raise PermissionDenied("Вы не можете удалить этот рецепт")
    recipe.delete()
    return redirect('recipe_catalog:index')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipe_catalog:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'recipe_catalog/register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('recipe_catalog:index')