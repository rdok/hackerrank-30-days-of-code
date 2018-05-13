from src.hackerrank.p03_strings.p07_text_wrap import text_wrap
from tests.test_case import TestCase


class TestTextWrap(TestCase):
    def setUp(self):
        self.script = text_wrap.__file__

    def test_default_case(self):
        actual = self.execute(self.script, 'ABCDEFGHIJKLIMNOQRSTUVWXYZ\n4\n')
        expected = 'ABCD\nEFGH\nIJKL\nIMNO\nQRST\nUVWX\nYZ\n'
        self.assertEquals(expected, actual)
