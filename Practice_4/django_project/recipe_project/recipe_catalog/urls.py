from django.urls import path
from .views import about, index, recipe_detail

urlpatterns = [
	path('', index, name='index'),
	path('about/', about, name='about'),
	path('recipe/<int:pk>/', recipe_detail, name='recipe_detail')
]