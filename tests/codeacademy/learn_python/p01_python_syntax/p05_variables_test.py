import datetime

from src.codeacademy.learn_python.p01_python_syntax import p05_variables
from tests.test_case import TestCase


class VariablesTest(TestCase):

    def test_it_sets_class_variables(self):
        expected = datetime.date.today()
        self.assertEqual(expected, p05_variables.todays_date)
