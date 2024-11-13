from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ValidationError

from recipe_catalog.models import Ingredient, Recipe, RecipeIngredient

class TestContent(TestCase):
	HOME_URL = reverse('recipe_catalog:index')
	RECIPES_ON_PAGE = 2

	RECIPE_NAME_SHTRUDEL = 'Штрудель'
	INGREDIENT_FLOUR_TITLE = 'Мука'
	INGREDIENT_SUGAR_TITLE = 'Сахар'
	INGREDIENT_APPLES_TITLE = 'Яблоки'
	INGREDIENT_BUTTER_TITLE = 'Масло сливочное'
	INGREDIENT_LEMON_TTILE = 'Лимонный сок'

	RECIPE_NAME_ITONSKAYA_PYTANICA = 'Итонская путаница'
	INGREDIENT_STRAWBERRY_TITLE = 'Клубника'
	INGREDIENT_CREAM_TITLE = 'Сливки'
	INGREDIENT_POWDERED_SUGAR_TITLE = 'Сахарная пудра'
	INGREDIENT_MERINGUE_TITLE = 'Безе'
	INGREDIENT_EXTRACT_TITLE = 'Ванильный экстракт'
	INGREDIENT_MINT_TITLE = 'Мята'

	@classmethod
	def setUpTestData(cls):
		cls.recipe_shtrudel = Recipe.objects.create(title=cls.RECIPE_NAME_SHTRUDEL)
		cls.ingredient_flour = Ingredient.objects.create(
			title=cls.INGREDIENT_FLOUR_TITLE,
			raw_weight=150,
			weight=140,
			cost=30
		)
		cls.ingredient_sugar = Ingredient.objects.create(
			title=cls.INGREDIENT_SUGAR_TITLE,
			raw_weight=50,
			weight=50,
			cost=15
		)
		cls.ingredient_apples = Ingredient.objects.create(
			title=cls.INGREDIENT_APPLES_TITLE,
			raw_weight=300,
			weight=280,
			cost=120
		)
		cls.ingredient_butter = Ingredient.objects.create(
			title=cls.INGREDIENT_BUTTER_TITLE,
			raw_weight=100,
			weight=90,
			cost=80
		)
		cls.ingredient_lemon = Ingredient.objects.create(
			title=cls.INGREDIENT_LEMON_TTILE,
			raw_weight=10,
			weight=10,
			cost=5
		)
		cls.recipe_shtrudel.ingredients.set([cls.ingredient_flour, cls.ingredient_sugar, cls.ingredient_apples,cls.ingredient_butter, cls.ingredient_lemon])

		cls.recipe_itonskaya_pytanica = Recipe.objects.create(title=cls.RECIPE_NAME_ITONSKAYA_PYTANICA)
		cls.ingredient_strawberry = Ingredient.objects.create(
			title=cls.INGREDIENT_STRAWBERRY_TITLE,
			raw_weight=500,
			weight=450,
			cost=200
		)
		cls.ingredient_cream = Ingredient.objects.create(
			title=cls.INGREDIENT_CREAM_TITLE,
			raw_weight=300,
			weight=300,
			cost=150
		)
		cls.ingredient_powdered_sugar = Ingredient.objects.create(
			title=cls.INGREDIENT_POWDERED_SUGAR_TITLE,
			raw_weight=50,
			weight=50,
			cost=20
		)
		cls.ingredient_meringue = Ingredient.objects.create(
			title=cls.INGREDIENT_MERINGUE_TITLE,
			raw_weight=200,
			weight=200,
			cost=100
		)
		cls.ingredient_extract = Ingredient.objects.create(
			title=cls.INGREDIENT_EXTRACT_TITLE,
			raw_weight=5,
			weight=5,
			cost=30
		)
		cls.ingredient_mint = Ingredient.objects.create(
			title=cls.INGREDIENT_MINT_TITLE,
			raw_weight=10,
			weight=10,
			cost=15
		)
		cls.recipe_itonskaya_pytanica.ingredients.set([cls.ingredient_strawberry, cls.ingredient_cream, cls.ingredient_powdered_sugar, cls.ingredient_meringue, cls.ingredient_extract, cls.ingredient_mint])


	
	def test_successful_create_recipe_ingredient(self):
		counts = [
			(self.recipe_shtrudel.ingredients.count(), 5, 'Рецепт'),
			(self.recipe_itonskaya_pytanica.ingredients.count(), 6, 'Рецепт'),
			(RecipeIngredient.objects.count(), 11,  'Ингредиент-Рецепт')
		]
		for count in counts:
			with self.subTest(message='Рецепты-Ингредиенты'):
				self.assertEqual(count[0], count[1], count[2])


	def test_home_count_recipes(self):
		response = self.client.get(self.HOME_URL)
		objects_list = response.context['recipes']
		recipes_count = objects_list.count()
		self.assertEqual(recipes_count, self.RECIPES_ON_PAGE)

	def test_add_new_recipe_and_check_count(self):
		new_recipe = Recipe.objects.create(title='Новый рецепт')
		response = self.client.get(self.HOME_URL)
		objects_list = response.context['recipes']
		recipes_count = objects_list.count()
		self.assertEqual(recipes_count, self.RECIPES_ON_PAGE + 1)
	
	def test_creation_recipe_with_invalid_title(self):
		invalid_recipe = Recipe.objects.create(title='Title12345')
		with self.assertRaises(ValidationError) as error:
			invalid_recipe.full_clean() 
		self.assertIn('Название должно быть строковым значением', error.exception.message_dict['title'])
	
	def test_creation_ingredient_with_invalid_title(self):
		ingredient_invalid_title = Ingredient.objects.create(
			title='sda231',
			raw_weight=120,
			weight=100,
			cost=80
		)
		with self.assertRaises(ValidationError) as error:
			ingredient_invalid_title.full_clean()
		self.assertIn('Название должно быть строковым значением', error.exception.message_dict['title'])
	
	def test_creation_ingredient_with_invalid_raw_weight(self):
		ingredient_invalid_raw_weight = Ingredient.objects.create(
			title='Test ingredient',
			raw_weight=-120,
			weight=100,
			cost=80
		)
		with self.assertRaises(ValidationError) as error:
			ingredient_invalid_raw_weight.full_clean()
		self.assertIn('Сырой вес должен быть положительным числом', error.exception.message_dict['raw_weight'])
	
	def test_creation_ingredient_with_invalid_weight(self):
		ingredient_invalid_weight = Ingredient(
			title='Test ingredient',
			raw_weight=120,
			weight='sdfsdf',
			cost=80
		)
		with self.assertRaises(ValidationError) as error:
			ingredient_invalid_weight.full_clean()
		self.assertIn('weight', error.exception.message_dict)
	
	def test_creation_ingredient_with_invalid_cost(self):
		ingredient_invalid_cost = Ingredient.objects.create(
			title='Test ingredient',
			raw_weight=120,
			weight=100,
			cost=-2423
		)
		with self.assertRaises(ValidationError) as error:
			ingredient_invalid_cost.full_clean()
		self.assertIn('Цена должна быть положительным числом', error.exception.message_dict['cost'])
	
	def test_recipe_shtrudel_weight_on_page(self):
		url = reverse('recipe_catalog:recipe_detail', args=[self.recipe_shtrudel.pk])
		response = self.client.get(url)
		expected_sum_weight = self.ingredient_flour.weight + self.ingredient_sugar.weight + self.ingredient_apples.weight + self.ingredient_butter.weight + self.ingredient_lemon.weight
		self.assertContains(response, f'Вес: {expected_sum_weight}')
	
	def test_recipe_itonskaya_pytanica_weight_on_page(self):
		url = reverse('recipe_catalog:recipe_detail', args=[self.recipe_itonskaya_pytanica.pk])
		response = self.client.get(url)
		expected_sum_weight = self.ingredient_strawberry.weight + self.ingredient_cream.weight + self.ingredient_powdered_sugar.weight + self.ingredient_meringue.weight + self.ingredient_extract.weight + self.ingredient_mint.weight
		self.assertContains(response, f'Вес: {expected_sum_weight}')
	
	def test_ingredients_shtrudel_are_sorted(self):
		url = reverse('recipe_catalog:recipe_detail', args=[self.recipe_shtrudel.pk])
		response = self.client.get(url)
		ingredients = response.context['ingredients']
		ingredient_titles = [ingredient.title for ingredient in ingredients]
		self.assertEqual(ingredient_titles, sorted(ingredient_titles))
	
	def test_ingredients_itonskaya_pytanica_are_sorted(self):
		url = reverse('recipe_catalog:recipe_detail', args=[self.recipe_itonskaya_pytanica.pk])
		response = self.client.get(url)
		ingredients = response.context['ingredients']
		ingredient_titles = [ingredient.title for ingredient in ingredients]
		self.assertEqual(ingredient_titles, sorted(ingredient_titles))
