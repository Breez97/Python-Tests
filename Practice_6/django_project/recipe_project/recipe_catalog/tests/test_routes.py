from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from http import HTTPStatus

from recipe_catalog.models import Ingredient, Recipe, RecipeIngredient, MeasurementUnit


User = get_user_model()


class TestRoutes(TestCase):
	INDEX_URL = reverse('recipe_catalog:index')
	ABOUT_URL = reverse('recipe_catalog:about')
	RECIPE_TITLE = 'Штрудель'
	INGREDIENT_SUGAR_TITLE = 'Сахар'
	ADMIN_URL = '/admin/'

	RECIPE_NAME_SHTRUDEL = 'Штрудель'
	INGREDIENT_FLOUR_TITLE = 'Мука'
	INGREDIENT_SUGAR_TITLE = 'Сахар'
	INGREDIENT_APPLES_TITLE = 'Яблоки'
	INGREDIENT_BUTTER_TITLE = 'Масло сливочное'
	INGREDIENT_LEMON_TITLE = 'Лимонный сок'

	@classmethod
	def setUpTestData(cls):

		cls.anonim_user = User.objects.create(username='anonimUser')
		cls.admin = User.objects.create(username='admin', is_staff=True)

		cls.grams_unit = MeasurementUnit.objects.create(
			title='Грамм',
			symbol='г',
			grams_per_unit=1
		)

		cls.recipe_shtrudel = Recipe.objects.create(title=cls.RECIPE_NAME_SHTRUDEL)

		cls.ingredient_flour = Ingredient.objects.create(
			title=cls.INGREDIENT_FLOUR_TITLE,
			measurement_unit=cls.grams_unit,
			total_weight=140,
			cost=30
		)
		cls.ingredient_sugar = Ingredient.objects.create(
			title=cls.INGREDIENT_SUGAR_TITLE,
			measurement_unit=cls.grams_unit,
			total_weight=50,
			cost=15
		)
		cls.ingredient_apples = Ingredient.objects.create(
			title=cls.INGREDIENT_APPLES_TITLE,
			measurement_unit=cls.grams_unit,
			total_weight=280,
			cost=120
		)
		cls.ingredient_butter = Ingredient.objects.create(
			title=cls.INGREDIENT_BUTTER_TITLE,
			measurement_unit=cls.grams_unit,
			total_weight=90,
			cost=80
		)
		cls.ingredient_lemon = Ingredient.objects.create(
			title=cls.INGREDIENT_LEMON_TITLE,
			measurement_unit=cls.grams_unit,
			total_weight=10,
			cost=5
		)
		cls.recipe_shtrudel.ingredients.set([
			cls.ingredient_flour,
			cls.ingredient_sugar,
			cls.ingredient_apples,
			cls.ingredient_butter,
			cls.ingredient_lemon
		])

	def setUp(self):
		self.client_anonim = Client()
		self.client_admin = Client()
		self.client_admin.force_login(self.admin)

	def test_home_page_anonim_user(self):
		response = self.client_anonim.get(self.INDEX_URL)
		self.assertEqual(response.status_code, HTTPStatus.OK)

	def test_home_page_admin_user(self):
		response = self.client_admin.get(self.INDEX_URL)
		self.assertEqual(response.status_code, HTTPStatus.OK)

	def test_about_page_anonim_user(self):
		response = self.client_anonim.get(self.ABOUT_URL)
		self.assertEqual(response.status_code, HTTPStatus.OK)

	def test_about_page_admin_user(self):
		response = self.client_admin.get(self.ABOUT_URL)
		self.assertEqual(response.status_code, HTTPStatus.OK)

	def test_detail_page_anonim_user(self):
		url = reverse('recipe_catalog:recipe_detail', args=[self.recipe_shtrudel.pk])
		response = self.client_anonim.get(url)
		self.assertEqual(response.status_code, HTTPStatus.OK)

	def test_detail_page_admin_user(self):
		url = reverse('recipe_catalog:recipe_detail', args=[self.recipe_shtrudel.pk])
		response = self.client_admin.get(url)
		self.assertEqual(response.status_code, HTTPStatus.OK)

	def test_admin_panel_access(self):
		response = self.client_admin.get(self.ADMIN_URL)
		self.assertEqual(response.status_code, HTTPStatus.OK)

	def test_admin_panel_access_anonymous(self):
		response = self.client_anonim.get(self.ADMIN_URL)
		self.assertEqual(response.status_code, HTTPStatus.FOUND)