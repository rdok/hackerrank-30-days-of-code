from src.p03_strings.p04_find_a_string import find_a_string
from tests.test_case import TestCase


class TestFindAString(TestCase):
    def setUp(self):
        self.script = find_a_string.__file__

    def test_default_case(self):
        actual = self.execute(self.script, 'ABCDCDC\nCDC\n')

        self.assertEquals('2\n', actual)