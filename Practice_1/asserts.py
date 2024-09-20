def quad_func(a, b, c, x):
	return a * x**2 + b * x + c


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


if __name__ == '__main__':
	test_1([1, -4, 0, 1])
	test_2([-0.5, -3, -2.5, 3])
	test_3([-0.25, -1, 3, 12])
	test_4()
	test_5()
