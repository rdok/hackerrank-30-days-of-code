from src.hackerrank.p01_introduction.p04_arithmetic_operators import arithmetic_operators
from tests.test_case import TestCase


class TestArithmeticOperators(TestCase):

    def setUp(self):
        self.script = arithmetic_operators.__file__

    def test_first_set_of_sum_of_numbers(self):
        actual_output = self.execute(self.script, '1\n3\n')

        self.assertEquals('4\n-2\n3\n', actual_output)

    def test_second_set_of_sum_of_numbers(self):
        actual_output = self.execute(self.script, '3\n2\n')

        self.assertEquals('5\n1\n6\n', actual_output)
