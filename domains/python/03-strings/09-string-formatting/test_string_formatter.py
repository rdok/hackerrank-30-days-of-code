import unittest

from string_formatter import *


class StringFormatterTest(unittest.TestCase):
    # def test_it_stores_the_processed_number(self):
    #     expected = 10
    #     string_formatter = StringFormatter(expected)
    #
    #     self.assertEqual(expected, string_formatter.number)
    #
    # def test_it_prints_the_required_number_as_the_object_string(self):
    #     expected = '''1 1 1 1'''
    #     string_formatter = StringFormatter(1)
    #
    #     self.assertEqual(expected, str(string_formatter))

    def test_it_formats_a_specific_number(self):
        expected = '  2  2  2 10'

        string_formatter = StringFormatter.format(2)

        self.assertEqual(expected, str(string_formatter))
