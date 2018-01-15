import os
import subprocess
import unittest

from ddt import ddt, data, unpack


@ddt
class TestArithmeticOperators(unittest.TestCase):
    @unpack
    @data({'first': 1, 'second': 3, 'total': 4, 'diff': -2, 'product': 3},
          {'first': 3, 'second': 2, 'total': 5, 'diff': 1, 'product': 6})
    def test_sum_of_numbers(self, first, second, total, diff, product):
        communication_input = str(first) + '\n' + str(second) + '\n'
        actual_output = self.process.communicate(communication_input)[0]
        expected = str(total) + '\n' + str(diff) + '\n' + str(product) + '\n'

        self.assertEquals(expected, actual_output)

    def setUp(self):
        script = os.path.dirname(os.path.realpath(__file__)) \
                 + "/arithmetic_operators.py"

        self.process = subprocess.Popen(
            ["python", script],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )

    def tearDown(self):
        self.process = None


if __name__ == '__main__':
    unittest.main()
