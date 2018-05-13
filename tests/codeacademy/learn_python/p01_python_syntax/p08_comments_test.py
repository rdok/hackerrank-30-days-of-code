import inspect

from src.codeacademy.learn_python.p01_python_syntax import p08_comments
from tests.test_case import TestCase


class CommentsTest(TestCase):
    def test_it_has_docs(self):
        expected =  '# Sentence with docs.\n'

        actual  = inspect.getcomments(p08_comments)

        self.assertEqual(expected, actual)
