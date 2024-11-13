from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from http import HTTPStatus

from recipe_catalog.models import Ingredient, Recipe, RecipeIngredient


User = get_user_model()


class TestRoutes(TestCase):
	INDEX_URL = reverse('recipe_catalog:index')
	ABOUT_URL = reverse('recipe_catalog:about')
	RECIPE_TITLE = 'Штрудель'
	INGREDIENT_SUGAR_TITLE = 'Сахар'
	ADMIN_URL = '/admin/'

	@classmethod
	def setUpTestData(cls):
		cls.anonim_user = User.objects.create(username='anonimUser')
		cls.admin = User.objects.create(username='admin', is_staff=True)

		cls.ingredient_sugar = Ingredient.objects.create(
			title=cls.INGREDIENT_SUGAR_TITLE,
			raw_weight=50,
			weight=50,
			cost=15
		)
		cls.recipe = Recipe.objects.create(
			title=cls.RECIPE_TITLE
		)
		cls.recipe.ingredients.set([cls.ingredient_sugar])

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
		url = reverse('recipe_catalog:recipe_detail', args=[self.recipe.pk])
		response = self.client_anonim.get(url)
		self.assertEqual(response.status_code, HTTPStatus.OK)

	def test_detail_page_admin_user(self):
		url = reverse('recipe_catalog:recipe_detail', args=[self.recipe.pk])
		response = self.client_admin.get(url)
		self.assertEqual(response.status_code, HTTPStatus.OK)

	def test_admin_panel_access(self):
		response = self.client_admin.get(self.ADMIN_URL)
		self.assertEqual(response.status_code, HTTPStatus.OK)

	def test_admin_panel_access_anonymous(self):
		response = self.client_anonim.get(self.ADMIN_URL)
		self.assertEqual(response.status_code, HTTPStatus.FOUND)
