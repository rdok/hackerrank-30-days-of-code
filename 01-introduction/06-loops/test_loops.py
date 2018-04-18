import os
import subprocess
import unittest

from ddt import ddt, data, unpack


@ddt
class TestDivision(unittest.TestCase):
    def setUp(self):
        script = os.path.dirname(os.path.realpath(__file__)) + "/loops.py"

        self.process = subprocess.Popen(["python", script],
                                        stdout=subprocess.PIPE,
                                        stdin=subprocess.PIPE,
                                        stderr=subprocess.STDOUT)

    def tearDown(self):
        self.process = None

    @data(['1\n', '0\n'],
          ['2\n', '0\n1\n'],
          ['3\n', '0\n1\n4\n'],
          ['5\n', '0\n1\n4\n9\n16\n'],
          ['20\n',
           '0\n1\n4\n9\n16\n25\n36\n49\n64\n81\n100\n121\n144\n169\n196\n225'
           '\n256\n289\n324\n361\n'])
    @unpack
    def test_one(self, user_input, expected_output):
        actual_output = self.process.communicate(input=user_input)[0]

        self.assertEquals(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
