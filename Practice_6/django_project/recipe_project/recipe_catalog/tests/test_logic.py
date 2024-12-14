from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from recipe_catalog.models import Recipe, Ingredient, MeasurementUnit


class RecipeTestCase(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='testuser', password='testpassword')
		self.other_user = User.objects.create_user(username='otheruser', password='otherpassword')
		self.recipe = Recipe.objects.create(title="Test Recipe", author=self.user)
		self.some_measurement_unit = MeasurementUnit.objects.create(
			title="Килограграмм",
			symbol="g",
			grams_per_unit=1.0
		)
		self.ingredient = Ingredient.objects.create(
			title="Test Ingredient", 
			author=self.user,
			total_weight=100.0, 
			measurement_unit=self.some_measurement_unit,
			cost=50.0 
		)


	def test_create_recipe_logged_in(self):
		self.client.login(username='testuser', password='testpassword')
		response = self.client.get(reverse('recipe_catalog:recipe_add'))
		self.assertEqual(response.status_code, 200)

	def test_edit_recipe_as_author(self):
		self.client.login(username='testuser', password='testpassword')
		response = self.client.get(reverse('recipe_catalog:recipe_edit', kwargs={'pk': self.recipe.pk}))
		self.assertEqual(response.status_code, 200)

	def test_edit_recipe_as_non_author(self):
		self.client.login(username='otheruser', password='otherpassword')
		response = self.client.get(reverse('recipe_catalog:recipe_edit', kwargs={'pk': self.recipe.pk}))
		self.assertEqual(response.status_code, 403)

	def test_delete_recipe_as_author(self):
		self.client.login(username='testuser', password='testpassword')
		response = self.client.post(reverse('recipe_catalog:recipe_delete', kwargs={'pk': self.recipe.pk}))
		self.assertRedirects(response, reverse('recipe_catalog:index'))

	def test_delete_recipe_as_non_author(self):
		self.client.login(username='otheruser', password='otherpassword')
		response = self.client.post(reverse('recipe_catalog:recipe_delete', kwargs={'pk': self.recipe.pk}))
		self.assertEqual(response.status_code, 403)

	def test_edit_ingredient_as_author(self):
		self.client.login(username='testuser', password='testpassword')
		response = self.client.get(reverse('recipe_catalog:ingredient_edit', kwargs={'pk': self.ingredient.pk}))
		self.assertEqual(response.status_code, 200)

	def test_edit_ingredient_as_non_author(self):
		self.client.login(username='otheruser', password='otherpassword')
		response = self.client.get(reverse('recipe_catalog:ingredient_edit', kwargs={'pk': self.ingredient.pk}))
		self.assertEqual(response.status_code, 403)

	def test_delete_ingredient_as_author(self):
		self.client.login(username='testuser', password='testpassword')
		response = self.client.post(reverse('recipe_catalog:ingredient_delete', kwargs={'pk': self.ingredient.pk}))
		self.assertRedirects(response, reverse('recipe_catalog:ingredients'))

	def test_delete_ingredient_as_non_author(self):
		self.client.login(username='otheruser', password='otherpassword')
		response = self.client.post(reverse('recipe_catalog:ingredient_delete', kwargs={'pk': self.ingredient.pk}))
		self.assertEqual(response.status_code, 403)
