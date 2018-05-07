from src.p03_strings.p01_swap_case import swap_case
from tests.test_case import TestCase


class TestSwapCase(TestCase):
    def setUp(self):
        self.script = swap_case.__file__

    def test_default_case(self):
        user_input = 'HackerRank.com presents "Pythonist 2".\n'
        actual = self.execute(self.script, user_input)

        self.assertEquals('hACKERrANK.COM PRESENTS "pYTHONIST 2".\n', actual)
