from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from django.core.exceptions import ValidationError
from decimal import Decimal


class MeasurementUnit(models.Model):
	title = models.CharField(
		max_length=50,
		unique=True,
		validators=[
			RegexValidator(
				regex=r'^[A-Za-zА-Яа-яёЁ\s]+$',
				message='Название должно быть строковым значением'
			)
		],
		verbose_name="Название"
	)
	symbol = models.CharField(
		max_length=10,
		verbose_name="Символ"
	)
	grams_per_unit = models.DecimalField(
		max_digits=10,
		decimal_places=2,
		validators=[
			MinValueValidator(
				limit_value=0.01,
				message='Вес должен быть положительным числом'
			)
		],
		verbose_name="Вес в граммах"
	)

	def __str__(self):
		return f"{self.title} ({self.symbol}) - {self.grams_per_unit}г"


class Ingredient(models.Model):
	title = models.CharField(
		max_length=255,
		validators=[
			RegexValidator(
				regex=r'^[A-Za-zА-Яа-яёЁ\s]+$',
				message='Название должно быть строковым значением'
			)
		],
		verbose_name="Название"
	)
	measurement_unit = models.ForeignKey(
		MeasurementUnit,
		on_delete=models.PROTECT,
		verbose_name="Единица измерения"
	)
	total_weight = models.DecimalField(
		max_digits=10,
		decimal_places=2,
		validators=[
			MinValueValidator(
				limit_value=0.1,
				message='Вес должен быть положительным числом'
			)
		],
		verbose_name="Общий вес в граммах"
	)
	cost = models.DecimalField(
		max_digits=10,
		decimal_places=2,
		validators=[
			MinValueValidator(
				limit_value=0.1,
				message='Цена должна быть положительным числом'
			)
		],
		verbose_name="Цена"
	)

	@property
	def quantity_in_units(self):
		if self.measurement_unit.grams_per_unit:
			return self.total_weight / self.measurement_unit.grams_per_unit
		return 0

	def __str__(self):
		return (
			f'{self.title} '
			f'({self.quantity_in_units:.2f} {self.measurement_unit.symbol}, '
			f'{self.total_weight}г, '
			f'{self.cost}₽)'
		)


class Recipe(models.Model):
	title = models.CharField(
		max_length=300,
		validators=[
			RegexValidator(
				regex=r'^[A-Za-zА-Яа-яёЁ\s]+$',
				message='Название должно быть строковым значением'
			)
		],
		verbose_name="Название"
	)
	ingredients = models.ManyToManyField(
		Ingredient,
		through="RecipeIngredient",
		verbose_name="Ингредиенты"
	)


class RecipeIngredient(models.Model):
	recipe = models.ForeignKey(
		Recipe,
		on_delete=models.CASCADE,
		verbose_name="Рецепт"
	)
	ingredient = models.ForeignKey(
		Ingredient,
		on_delete=models.CASCADE,
		verbose_name="Ингредиент"
	)

	def __str__(self):
		return f'{self.recipe.title} - {self.ingredient.title}'

	class Meta:
		verbose_name = "Ингредиент в рецепте"
		verbose_name_plural = "Ингредиенты в рецепте"
		constraints = [
			models.UniqueConstraint(
				fields=['recipe', 'ingredient'],
				name='unique_recipes_ingredients'
			)
		]