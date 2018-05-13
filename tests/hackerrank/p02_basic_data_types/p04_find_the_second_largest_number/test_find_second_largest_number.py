from src.hackerrank.p02_basic_data_types.p04_find_the_second_largest_number import find_second_largest_number

from tests.test_case import TestCase


class TestFindSecondLargestNumber(TestCase):

    def setUp(self):
        self.script = find_second_largest_number.__file__

    def test_positive_numbers(self):
        actual = self.execute(self.script, '5\n2 3 6 5')
        self.assertEquals('5\n', actual)

    def test_positive_numbers_with_multiple_max_occurances(self):
        actual = self.execute(self.script, '5\n2 3 6 6 5')
        self.assertEquals('5\n', actual)

    def test_positive_and_negative_numbers(self):
        actual = self.execute(self.script, '5\n2 3 6 -6 5')
        self.assertEquals('5\n', actual)

    def test_positive_and_negative_numbers_with_multiple_max_occurences(self):
        actual = self.execute(self.script, '5\n2 3 6 6 -6 5')
        self.assertEquals('5\n', actual)

    def test_negative_numbers(self):
        actual = self.execute(self.script, '5\n-2 -3 -6 -6 -5')
        self.assertEquals('-3\n', actual)

    def test_negative_numbers_with_multiple_occurences_of_max(self):
        actual = self.execute(self.script, '5\n-2 -2 -3 -6 -6 -5')
        self.assertEquals('-3\n', actual)