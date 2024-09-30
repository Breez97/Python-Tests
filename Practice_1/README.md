# Практическая работа №1: Doctest, Unittest, Asserts

## Содержание:

- [Введение](#введение)
- [Задание](#задание)
- [Ход работы](#ход-работы)
- [Тестирование](#тестирование)
	* [Тестирование с использованием `assert`](#тестирование-с-использованием-assert)
	* [Тестирование с использованием `doctest`](#тестирование-с-использованием-doctest)
	* [Тестирование с использованием `unittest`](#тестирование-с-использованием-unittest)


## Введение

Существует несколько подходов к тестированию:
- непосредственное использование инструкции `assert`,
- `doctest`,
- `unittest`,
- `pytest` и др. внешние инструменты

## Задание

В данной практической работе нужно использовать первые три подхода. Эти подходы доступны "из коробки" (не нужно устанавливать дополнительные пакеты).

Следует выбрать любой алгоритм: например, алгоритм сортировки, рассчёт значения функции (квадратичной, тригонометрической).

А потом протестировать тремя вариантами:
- непосредственно использовав инструкции `assert`,
- `doctest`,
- `unittest`.

## Ход работы

Для выполнения данной практической работы была написана функция для подсчета значений квадратичной функции:

``` Python
def quad_func(a, b, c, x):
	return a * x**2 + b * x + c
```

## Тестирование

#### Тестирование с использованием `assert`

Выполнение тестирования:

``` Python
def test_1(numbers):
	result = quad_func(*numbers)
	assert result == -3, f"Ожидалось -3, получено {result}"


def test_2(numbers):
	result = quad_func(*numbers)
	assert result == -16.0, f"Ожидалось -16.0, получено {result}"


def test_3(numbers):
	result = quad_func(*numbers)
	assert result == -45.0, f"Ожидалось -45.0, получено {result}"


def test_4():
	try:
		quad_func(4.23, 2)
	except TypeError as e:
		assert str(e) == "quad_func() missing 2 required positional arguments: 'c' and 'x'"
	else:
		assert False, "Ожидалось исключение TypeError"


def test_5():
	try:
		quad_func(1, 3, 2, 3, 4)
	except TypeError as e:
		assert str(e) == "quad_func() takes 4 positional arguments but 5 were given"
	else:
		assert False, "Ожидалось исключение TypeError"
```

#### Тестирование с использованием `doctest`

Выполнение тестирования:

``` Python
def quad_func(a, b, c, x):
	"""
	>>> quad_func(1, -4, 0, 1)
	-3

	>>> quad_func(-0.5, -3, -2.5, 3)
	-16.0

	>>> quad_func(-0.25, -1, 3, 12)
	-45.0

	>>> quad_func(4.23, 2)
	Traceback (most recent call last):
	TypeError: quad_func() missing 2 required positional arguments: 'c' and 'x'

	>>> quad_func(1, 3, 2, 3, 4)
	Traceback (most recent call last):
	TypeError: quad_func() takes 4 positional arguments but 5 were given
	"""
	return a * x**2 + b * x + c
```

#### Тестирование с использованием `unittest`

Выполнение тестирования:

``` Python
class TestQuadFunc(unittest.TestCase):

	def test_1(self):
		res = quad_func(3, -12, 9, -3)
		self.assertEqual(res, 72)
	
	def test_2(self):
		res = quad_func(0.5, -1, -1.5, -23.4)
		self.assertAlmostEqual(res, 295.68, places=2)
	
	def test_3(self):
		res = quad_func(0.3, -2, 1, -4.538)
		self.assertAlmostEqual(res, 16.25403, places=5)
	
	def test_4(self):
		with self.assertRaises(TypeError):
			res = quad_func(1, 2)
	
	def test_5(self):
		with self.assertRaises(TypeError):
			res = quad_func(1, 2, 4, 3, 4)
```