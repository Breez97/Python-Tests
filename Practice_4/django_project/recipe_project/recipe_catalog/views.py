from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.db.models import Sum 
from .models import Recipe


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
			'sum_weight': recipe.ingredients.aggregate(total=Sum('weight'))['total'],
			'sum_cost': recipe.ingredients.aggregate(total=Sum('cost'))['total']
		}
	)