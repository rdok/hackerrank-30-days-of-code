from src.p01_introduction.p08_print_function import print_function

from tests.test_case import TestCase


class TestPrintFunction(TestCase):
    def test_is_evenly_dived(self):
        script = print_function.__file__

        actual = self.execute(script, '3')

        self.assertEquals('123\n', actual)
