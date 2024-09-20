import unittest

def quad_func(a, b, c, x):
	return a * x**2 + b * x + c

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