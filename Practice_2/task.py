# (Ш)амров -> (Ш)трудель

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
			raise ValueError("Title must be string")
		self._title = value
	
	@property
	def raw_weight(self):
		return self._raw_weight
	
	@raw_weight.setter
	def raw_weight(self, value):
		if not isinstance(value, (int, float)) or value <= 0:
			raise ValueError("Raw weight must be a positive number")
		self._raw_weight = value
	
	@property
	def weight(self):
		return self._weight
	
	@weight.setter
	def weight(self, value):
		if not isinstance(value, (int, float)) or value <= 0:
			raise ValueError("Weight must be a positive number")
		self._weight = value
	
	@property
	def cost(self):
		return self._cost
	
	@cost.setter
	def cost(self, value):
		if not isinstance(value, (int, float)) or value <= 0:
			raise ValueError("Cost must be a positive number")
		self._cost = value;
	
	def __str__(self):
		return f'  {self.title}:\n    Raw Weight: {self.raw_weight}\n    Weight: {self.weight}\n    Cost: {self.cost}'


class Receipt:
	def __init__(self, title:str, ingredients_list:list[tuple[str, (int, float), (int, float)]]) -> None:
		self.title = title;
		self.ingredients = []
		for ingredient_title, ingredient_raw_weigth, ingredient_weight, ingredient_cost in ingredients_list:
			self.ingredients.append(Ingredient(ingredient_title, ingredient_raw_weigth, ingredient_weight, ingredient_cost))
	
	@property
	def title(self):
		return self._title
	
	@title.setter
	def title(self, value):
		if not isinstance(value, str):
			raise ValueError("Title must be string")
		self._title = value;
	
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
		ingredients_str = "\n".join(str(ingredient) for ingredient in self.ingredients)
		return f'Receipt: {self.title}\nIngredients:\n{ingredients_str}'


if __name__ == '__main__':
	receipt_from_api = {
        "title": "Яичница с беконом и помидорами.",
        "ingredients_list": [
            ('Яйцо', 80, 70, 20),
            ('Бекон', 200, 100, 300),
            ('Помидор', 100, 80, 200),
        ],
    }

	receipt = Receipt(receipt_from_api['title'], receipt_from_api['ingredients_list'])
	print(receipt.calc_raw_weight())
	print(receipt.__str__())

	# ingredient = Ingredient("Test", 0.3, 100)
	
	# print(ingredient.title)
	# print(ingredient.weight)
	# print(ingredient.cost)
