from sys import platform

from src.hackerrank.p02_basic_data_types.p02_tuples import tuples
from tests.test_case import TestCase


class TestTuples(TestCase):
    def setUp(self):
        self.script = tuples.__file__

    def test_default_use_case(self):
        actual = self.execute(self.script, '2\n1 2\n')
        expected = '1299869600' if platform == "win32" else '3713081631934410656'
        self.assertEquals(expected + '\n', actual)
