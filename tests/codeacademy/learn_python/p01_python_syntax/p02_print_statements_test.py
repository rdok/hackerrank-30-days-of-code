from src.codeacademy.learn_python.p01_python_syntax import p02_print_statements
from tests.test_case import TestCase


class PrintStatementsTest(TestCase):

    def setUp(self):
        self.script = p02_print_statements.__file__

    def test_it_print_function_with_parenthesis(self):
        actual_output = self.execute(self.script)

        expected = "test\n"

        self.assertEqual(expected, actual_output)
