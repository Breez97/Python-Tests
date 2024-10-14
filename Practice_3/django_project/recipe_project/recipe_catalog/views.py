from django.shortcuts import render
from django.http import HttpResponse, Http404
from .constants import recipes


def index(request):
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
	recipe = next((r for r in recipes if r.id == pk), None)
	if recipe is None:
		raise Http404("Recipe does not exist")
	return render(
		request=request,
		template_name='recipe_catalog/recipe_detail.html',
		context={'recipe': recipe}
	)