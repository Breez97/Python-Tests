from .models import Receipe

recipes = [
	Receipe(1, 'Штрудель', [
		('Мука', 150, 140, 30),
		('Сахар', 50, 50, 15),
		('Яблоки', 300, 280, 120),
		('Масло сливочное', 100, 90, 80),
		('Корица', 5, 5, 10),
		('Лимонный сок', 10, 10, 5),
	]),
	Receipe(2, 'Итонская путаница', [
		('Клубника', 500, 450, 200),
		('Сливки', 300, 300, 150),
		('Сахарная пудра', 50, 50, 20),
		('Безе', 200, 200, 100),
		('Ванильный экстракт', 5, 5, 30),
		('Мята', 10, 10, 15),
	])
]
