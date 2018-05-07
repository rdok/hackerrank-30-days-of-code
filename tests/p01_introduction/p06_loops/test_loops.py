from src.p01_introduction.p06_loops import loops

from tests.test_case import TestCase


class TestDivision(TestCase):
    def setUp(self):
        self.script = loops.__file__

    def test_first_case(self):
        actual = self.execute(self.script, '1\n')
        self.assertEquals('0\n', actual)

    def test_second_case(self):
        actual = self.execute(self.script, '2\n')
        self.assertEquals('0\n1\n', actual)

    def test_third_case(self):
        actual = self.execute(self.script, '3\n')
        self.assertEquals('0\n1\n4\n', actual)

    def test_fourth_case(self):
        actual = self.execute(self.script, '5\n')
        self.assertEquals('0\n1\n4\n9\n16\n', actual)

    def test_fifth_case(self):
        expected = '0\n1\n4\n9\n16\n25\n36\n49\n64\n81\n100\n121\n144\n169\n196\n225\n256\n289\n324\n361\n'
        actual = self.execute(self.script, '20\n')
        self.assertEquals(expected, actual)
