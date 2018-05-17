from src.codeacademy.learn_python.p01_python_syntax import p09_numbers
from tests.test_case import TestCase


class NumbersTest(TestCase):
    def setUp(self):
        self.cucumbers = 2
        self.minimum_cucumbers = 1
        self.price_per_cucumber = 3.25
        self.total_cost = self.cucumbers * self.price_per_cucumber
        self.script = p09_numbers.__file__

    def test_it_stores_the_number_of_cucumbers(self):
        cucumbers = p09_numbers.cucumbers
        self.assertIsInstance(cucumbers, int)
        self.assertGreater(cucumbers, self.minimum_cucumbers)

    def test_it_stores_the_price_per_cucumber(self):
        actual = p09_numbers.price_per_cucumber
        self.assertIsInstance(actual, float)
        self.assertEqual(self.price_per_cucumber, actual)

    def test_it_stores_the_total_cost(self):
        actual = p09_numbers.total_cost
        self.assertIsInstance(actual, float)
        self.assertEqual(self.total_cost, actual)

    def test_it_prints_the_total_cost(self):
        actual = self.execute(self.script)
        expected = str(self.total_cost) + "\n"
        self.assertEqual(expected, actual)
