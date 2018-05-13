from tests.test_case import TestCase
from src.codeacademy.learn_python.p01_python_syntax.p04_handling_errors import HandlingErrors


class HandlingErrorsTest(TestCase):

    def test_it_throws_exception(self):
        syntaxError = HandlingErrors()

        with self.assertRaises(SyntaxError) as context:
            syntaxError.throw_error()

        self.assertTrue('SyntaxError raised.' in context.exception)