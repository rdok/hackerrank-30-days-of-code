import unittest

from src.p03_strings.p09_string_formatting.string_formatter import StringFormatter


class StringFormatterTest(unittest.TestCase):
    def test_it_stores_the_processed_number(self):
        expected = 10
        string_formatter = StringFormatter(expected)

        self.assertEqual(expected, string_formatter.number)

    def test_it_prints_the_required_number_as_the_object_string(self):
        self.assertEqual('1 1 1 1', str(StringFormatter(1)))

    def test_it_formats_a_specific_number(self):
        self.assertEqual(' 2  2  2 10', str(StringFormatter.format(2, 2)))

    def test_it_formats_a_number(self):
        self.assertEqual(' 1  1  1  1\n 2  2  2 10', str(StringFormatter(2)))

    def test_it_formats_the_requested_number(self):
        actual = str(StringFormatter(17))
        expected = '''    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001'''

        self.assertEqual(
            expected, actual,
            'Failed asserting expected \n{}\n equals \n{}\n'.format(expected, actual)
        )
