from src.hackerrank.p01_introduction.p05_division import division

from tests.test_case import TestCase


class TestDivision(TestCase):

    def setUp(self):
        self.script = division.__file__

    def test_division_types(self):
        expected_output = '1\n1.33333333333\n'
        actual_output = self.execute(self.script, '4\n3\n')

        self.assertEquals(expected_output, actual_output)
