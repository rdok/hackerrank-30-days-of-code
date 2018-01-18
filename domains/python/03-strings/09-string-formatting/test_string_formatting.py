import os
import subprocess
import unittest

from ddt import ddt


@ddt
class TestStringFormatting(unittest.TestCase):
    def test_greeting(self):
        script = os.path.dirname(
            os.path.realpath(__file__)) + "/string_formatting.py"

        process = subprocess.Popen(["python", script],
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)

        actual_output = process.communicate('17')[0]
        self.assertEquals('Hello James Potter! You just delved into python.\n',
                          actual_output)


if __name__ == '__main__':
    unittest.main()
