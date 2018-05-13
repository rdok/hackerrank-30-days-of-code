from tests.test_case import TestCase
from src.codeacademy.learn_python.p01_python_syntax import  p07_updating_variables


class UpdatingVariablesTest(TestCase):

    def test_it_calculates_the_annual_rainfall(self):
        expected = 45.209999999999994

        self.assertEqual(expected, p07_updating_variables.annual_rainfall)