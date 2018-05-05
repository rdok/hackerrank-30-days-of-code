import os
import subprocess
import unittest


class TestStringFormatting(unittest.TestCase):
    def test_greeting(self):
        script = os.path.dirname(
            os.path.realpath(__file__)) + "/string_formatting_script.py"

        process = subprocess.Popen(["python", script],
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        actual_output = process.communicate('17')[0]

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

        self.assertTrue(
            expected in actual_output,
            'Failed asserting expected \n{}\n equals actual \n{}\n'.format(
                expected, actual_output
            )
        )
