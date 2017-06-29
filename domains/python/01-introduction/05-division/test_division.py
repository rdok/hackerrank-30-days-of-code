import subprocess
import unittest

from ddt import ddt, data, unpack


@ddt
class TestDivision(unittest.TestCase):
    @unpack
    @data(['4', '3', '1\n1.33333333333\n'])
    def test_division_types(self, first_input, second_input, expected_output):
        process = subprocess.Popen(["python", "division.py"],
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)

        actual_ouput = \
            process.communicate(
                input=first_input + '\n' + second_input + '\n'
            )[0]

        self.assertEquals(expected_output, actual_ouput)


if __name__ == '__main__':
    unittest.main()
