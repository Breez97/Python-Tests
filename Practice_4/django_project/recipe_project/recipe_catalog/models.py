from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from django.core.exceptions import ValidationError


class Ingredient(models.Model):
	title = models.CharField(
		max_length=255,
		validators=[
			RegexValidator(
				regex=r'^[A-Za-zА-Яа-яёЁ\s]+$',
				message='Название должно быть строковым значением'
			)
		]
	)
	raw_weight = models.FloatField(
		validators=[
			MinValueValidator(
				limit_value=0.1,
				message='Сырой вес должен быть положительным числом'
			)
		]
	)
	weight = models.FloatField(
		validators=[
			MinValueValidator(
				limit_value=0.1,
				message='Вес должен быть положительным числом'
			)
		]
	)
	cost = models.FloatField(
		validators=[
			MinValueValidator(
				limit_value=0.1,
				message='Цена должна быть положительным числом'
			)
		]
	)

	def __str__(self):
		return f'{self.title} (Сырой вес: {self.raw_weight} г, Вес: {self.weight} г, Цена: {self.cost} )'


class Recipe(models.Model):
	title = models.CharField(
		max_length=300,
		validators=[
			RegexValidator(
				regex=r'^[A-Za-zА-Яа-яёЁ\s]+$',
				message='Название должно быть строковым значением'
			)
		]
	)
	ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredient")

	def __str__(self):
		return self.title


class RecipeIngredient(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.recipe.title} - {self.ingredient.title}'
	
	class Meta:
		constraints = [
			models.UniqueConstraint(
				fields=['recipe', 'ingredient'],
				name='unique recipes ingredients'
			)
		]
