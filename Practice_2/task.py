class Ingredient:
	def __init__(self, title:str, raw_weight:(int, float), weight:(int, float), cost:(int, float)) -> None:
		self.title = title
		self.raw_weight = raw_weight
		self.weight = weight
		self.cost = cost

	@property
	def title(self):
		return self._title
	
	@title.setter
	def title(self, value):
		if not isinstance(value, str):
			raise ValueError('Название должно быть строковым значением')
		self._title = value
	
	@property
	def raw_weight(self):
		return self._raw_weight
	
	@raw_weight.setter
	def raw_weight(self, value):
		if not isinstance(value, (int, float)) or value <= 0:
			raise ValueError('Сырой вес должен быть положительным числом')
		self._raw_weight = value
	
	@property
	def weight(self):
		return self._weight
	
	@weight.setter
	def weight(self, value):
		if not isinstance(value, (int, float)) or value <= 0:
			raise ValueError('Вес должен быть положительным числом')
		self._weight = value
	
	@property
	def cost(self):
		return self._cost
	
	@cost.setter
	def cost(self, value):
		if not isinstance(value, (int, float)) or value <= 0:
			raise ValueError('Цена должна быть положительным числом')
		self._cost = value;
	
	def __str__(self):
		return f'  {self.title}:\n    Сырой вес: {self.raw_weight}\n    Вес: {self.weight}\n    Цена: {self.cost}'


class Receipt:
	def __init__(self, title:str, ingredients_list:list[tuple[str, (int, float), (int, float)]]) -> None:
		self.title = title;
		self.ingredients = [Ingredient(title, raw_weight, weight, cost) for title, raw_weight, weight, cost in ingredients_list]
	
	@property
	def title(self):
		return self._title
	
	@title.setter
	def title(self, value):
		if not isinstance(value, str):
			raise ValueError('Название должно быть строковым значением')
		self._title = value;
	
	@property
	def ingredients(self):
		return self._ingredients
	
	@ingredients.setter
	def ingredients(self, value):
		if not value:
			raise ValueError('Список ингредиентов не может быть пустым')
		if not all(isinstance(item, Ingredient) for item in value):
			raise ValueError('Все элементы списка должны быть объектами класса Ingredient')
		self._ingredients = value
	
	def calc_raw_weight(self, portions=1):
		result = 0
		for ingredient in self.ingredients:
			result += ingredient.raw_weight
		return result * portions
	
	def calc_weight(self, portions=1):
		result = 0
		for ingredient in self.ingredients:
			result += ingredient.weight
		return result * portions
	
	def calc_cost(self, portions=1):
		result = 0
		for ingredient in self.ingredients:
			result += ingredient.cost
		return result * portions
	
	def __str__(self):
		ingredients_str = '\n'.join(str(ingredient) for ingredient in self.ingredients)
		return f'Блюдо: {self.title}\nИгредиенты:\n{ingredients_str}'


if __name__ == '__main__':
	print('--------------------------------')
	
	# (Ш)амров -> (Ш)трудель
	receipt_from_api_surname = {
		'title': 'Штрудель',
		'ingredients_list': [
			('Мука', 150, 140, 30),
			('Сахар', 50, 50, 15),
			('Яблоки', 300, 280, 120),
			('Масло сливочное', 100, 90, 80),
			('Корица', 5, 5, 10),
			('Лимонный сок', 10, 10, 5),
		],
	}

	print('(Ш)амров -> (Ш)трудель\n')
	receipt_surname = Receipt(receipt_from_api_surname['title'], receipt_from_api_surname['ingredients_list'])
	print(receipt_surname.__str__())

	print('--------------------------------')

	# (И)лья -> (И)тонская путаница
	receipt_from_api_name = {
		'title': 'Итонская путаница',
		'ingredients_list': [
			('Клубника', 500, 450, 200),
			('Сливки', 300, 300, 150),
			('Сахарная пудра', 50, 50, 20),
			('Безе', 200, 200, 100),
			('Ванильный экстракт', 5, 5, 30),
			('Мята', 10, 10, 15)
		]
	}

	print('(И)лья -> (И)тонская путаница\n')
	receipt_name = Receipt(receipt_from_api_name['title'], receipt_from_api_name['ingredients_list'])
	print(receipt_name.__str__())
