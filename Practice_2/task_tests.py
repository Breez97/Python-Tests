import unittest
from task import Ingredient, Receipt

class TestIngredient(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.ingredient_data = {
			'title': 'Мука',
			'raw_weight': 150,
			'weight': 140,
			'cost': 30
		}
	
	def setUp(self):
		self.ingredient = Ingredient(
			self.ingredient_data['title'],
			self.ingredient_data['raw_weight'],
			self.ingredient_data['weight'],
			self.ingredient_data['cost']
		)
	
	def tearDown(self):
		del self.ingredient
	
	@classmethod
	def tearDownClass(cls):
		cls.ingredient_data = None

	def test_valid_ingredient(self):
		self.assertEqual(self.ingredient.title, 'Мука'),
		self.assertEqual(self.ingredient.raw_weight, 150),
		self.assertEqual(self.ingredient.weight, 140),
		self.assertEqual(self.ingredient.cost, 30)
	
	# Test title
	def test_title_setter(self):
		with self.assertRaises(ValueError):
			self.ingredient.title = 12
	
	# Test raw_weight
	def test_raw_weight_setter_1(self):
		with self.assertRaises(ValueError):
			self.ingredient.raw_weight = 'Строка'
	
	def test_raw_weight_setter_2(self):
		with self.assertRaises(ValueError):
			self.ingredient.raw_weight = -4543
	
	def test_raw_weight_setter_3(self):
		with self.assertRaises(ValueError):
			self.ingredient.raw_weight = 0
	
	# Test weight
	def test_weight_setter_1(self):
		with self.assertRaises(ValueError):
			self.ingredient.weight = 'Строка'
	
	def test_weight_setter_2(self):
		with self.assertRaises(ValueError):
			self.ingredient.weight = -93.12
	
	def test_weight_setter_3(self):
		with self.assertRaises(ValueError):
			self.ingredient.weight = 0
	
	# Test cost
	def test_cost_setter_1(self):
		with self.assertRaises(ValueError):
			self.ingredient.cost = 'Строка'
	def test_cost_setter_2(self):
		with self.assertRaises(ValueError):
			self.ingredient.cost = -35
	def test_cost_setter_3(self):
		with self.assertRaises(ValueError):
			self.ingredient.cost = 0
		
	# Test str method
	def test_str_method(self):
		expected = '  Мука:\n    Сырой вес: 150\n    Вес: 140\n    Цена: 30'
		self.assertEqual(str(self.ingredient), expected)


class TestReceiptSurname(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.receipt_title = 'Штрудель'
		cls.receipt_ingredients_data = [
			('Мука', 150, 140, 30),
			('Сахар', 50, 50, 15),
			('Яблоки', 300, 280, 120),
			('Масло сливочное', 100, 90, 80),
			('Корица', 5, 5, 10),
			('Лимонный сок', 10, 10, 5)
		]

	def setUp(self):
		self.receipt = Receipt(self.receipt_title, self.receipt_ingredients_data)

	def tearDown(self):
		del self.receipt

	@classmethod
	def tearDownClass(cls):
		cls.receipt_title = None
		cls.receipt_ingredients_data = None

	def test_valid_receipt(self):
		self.assertEqual(self.receipt.title, 'Штрудель')
		self.assertEqual(len(self.receipt.ingredients), 6)

	# Test title
	def test_title_setter(self):
		with self.assertRaises(ValueError):
			self.receipt.title = 453

	# Test calculations
	def test_calc_raw_weight(self):
		self.assertEqual(self.receipt.calc_raw_weight(), 615)
		self.assertEqual(self.receipt.calc_raw_weight(2), 1230)

	def test_calc_weight(self):
		self.assertEqual(self.receipt.calc_weight(), 575)
		self.assertEqual(self.receipt.calc_weight(3), 1725)

	def test_calc_cost(self):
		self.assertEqual(self.receipt.calc_cost(), 260)
		self.assertEqual(self.receipt.calc_cost(4), 1040)

	def test_empty_ingredients_list(self):
		with self.assertRaises(ValueError):
			Receipt('Пустой рецепт', [])

	def test_invalid_ingredient_type(self):
		invalid_ingredients = [('Мука', 150, 140, 30), 'Неправильный ингредиент']
		with self.assertRaises(ValueError):
			Receipt('Неправильный рецепт', invalid_ingredients)

	def test_zero_portions(self):
		self.assertEqual(self.receipt.calc_raw_weight(0), 0)
		self.assertEqual(self.receipt.calc_weight(0), 0)
		self.assertEqual(self.receipt.calc_cost(0), 0)


class TestReceiptName(unittest.TestCase):
	
	@classmethod
	def setUpClass(cls):
		cls.receipt_title = 'Итонская путаница'
		cls.receipt_ingredients_data = [
			('Клубника', 500, 450, 200),
			('Сливки', 300, 300, 150),
			('Сахарная пудра', 50, 50, 20),
			('Безе', 200, 200, 100),
			('Ванильный экстракт', 5, 5, 30),
			('Мята', 10, 10, 15)
		]

	def setUp(self):
		self.receipt = Receipt(self.receipt_title, self.receipt_ingredients_data)

	def tearDown(self):
		del self.receipt

	@classmethod
	def tearDownClass(cls):
		cls.receipt_title = None
		cls.receipt_ingredients_data = None
	
	# Test title
	def test_title_setter(self):
		with self.assertRaises(ValueError):
			self.receipt.title = -131
	
	# Test calculations
	def test_valid_receipt(self):
		self.assertEqual(self.receipt.title, 'Итонская путаница')
		self.assertEqual(len(self.receipt.ingredients), 6)

	def test_calc_raw_weight(self):
		self.assertEqual(self.receipt.calc_raw_weight(), 1065)
		self.assertEqual(self.receipt.calc_raw_weight(2), 2130)

	def test_calc_weight(self):
		self.assertEqual(self.receipt.calc_weight(), 1015)
		self.assertEqual(self.receipt.calc_weight(3), 3045)

	def test_calc_cost(self):
		self.assertEqual(self.receipt.calc_cost(), 515)
		self.assertEqual(self.receipt.calc_cost(4), 2060)
	
	def test_empty_ingredients_list(self):
		with self.assertRaises(ValueError):
			Receipt('Пустой рецепт', [])

	def test_invalid_ingredient_type(self):
		invalid_ingredients = [('Мука', 150, 140, 30), 'Неправильный ингредиент']
		with self.assertRaises(ValueError):
			Receipt('Неправильный рецепт', invalid_ingredients)

	def test_zero_portions(self):
		self.assertEqual(self.receipt.calc_raw_weight(0), 0)
		self.assertEqual(self.receipt.calc_weight(0), 0)
		self.assertEqual(self.receipt.calc_cost(0), 0)


if __name__ == '__main__':
	unittest.main()