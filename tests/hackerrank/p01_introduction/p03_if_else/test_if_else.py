import src.hackerrank.p01_introduction.p03_if_else.if_else as script

from tests.test_case import TestCase


class TestIfElse(TestCase):

    def setUp(self):
        self.script = script.__file__

    def test_weird_numbers(self):
        for element in ['1', '3', '6', '20']:
            self.assertEquals("Weird\n", self.execute(self.script, element))

    def test_normal_numbers(self):
        for element in ['2', '4', '22', '100']:
            self.assertEquals("Not Weird\n", self.execute(self.script, element))
