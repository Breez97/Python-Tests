from django.urls import path
from .views import about, index, recipe_detail

app_name = 'recipe_catalog'

urlpatterns = [
	path('', index, name='index'),
	path('about/', about, name='about'),
	path('recipe/<int:pk>/', recipe_detail, name='recipe_detail')
]