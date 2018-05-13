from tests.test_case import TestCase
from src.codeacademy.learn_python.p01_python_syntax import p05_variables
import datetime

class VariablesTest(TestCase):
    def setUp(self):
        self.script = p05_variables.__file__

    def test_it_sets_class_variables(self):
        expected = datetime.date.today()
        self.assertEqual(expected, p05_variables.todays_date)
