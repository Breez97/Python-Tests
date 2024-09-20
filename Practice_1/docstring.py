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


if __name__ == '__main__':
	import doctest
	doctest.testmod()
