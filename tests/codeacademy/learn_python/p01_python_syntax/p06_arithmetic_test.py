from tests.test_case import TestCase
from src.codeacademy.learn_python.p01_python_syntax import p06_arithmetic


class ArithmeticTest(TestCase):

    def setUp(self):
       self.script = p06_arithmetic.__file__

    def test_it_multiplies_two_numbers(self):
        self.assertEqual(10, p06_arithmetic.product)

