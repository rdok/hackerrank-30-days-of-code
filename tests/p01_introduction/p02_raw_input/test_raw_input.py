from src.p01_introduction.p02_raw_input import raw_input
from tests.test_case import TestCase


class TestRawInput(TestCase):

    def setUp(self):
        self.script = raw_input.__file__

    def test_prints_raw_input(self):
        expected_output = 'How many chickens does it take to cross the road?\n'
        actual_output = self.execute(self.script, expected_output)

        self.assertEquals(expected_output, actual_output)
