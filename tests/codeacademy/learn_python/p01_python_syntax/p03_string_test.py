from tests.test_case import TestCase
from src.codeacademy.learn_python.p01_python_syntax import p03_string


class StringTest(TestCase):

    def setUp(self):
        self.script =  p03_string.__file__

    def test_print_string_using_plus_operator(self):
        expected = 'Hello Chosen One\n1'

        actual = self.execute(self.script)

        self.assertEqual(expected, actual)