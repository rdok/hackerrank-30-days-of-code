import subprocess
import unittest

from ddt import ddt, data, unpack


@ddt
class TestArithmetciOperators(unittest.TestCase):
    @unpack
    @data(
        {
            'firstInput': '1', 'secondInput': '3', 'total': '4',
            'difference': '-2', 'product': '3'
        },
        {
            'firstInput': '3', 'secondInput': '2', 'total': '5',
            'difference': '1', 'product': '6'
        }
    )
    def test_sum_of_numbers(self, first_input, second_input, total, difference,
                            product):
        process = subprocess.Popen(["python", "arithmetic_operators.py"],
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)

        actual_output = \
            process.communicate(
                input=first_input + '\n' + second_input + '\n'
            )[0]

        self.assertEquals(
            total + '\n' + difference + '\n' + product + '\n',
            actual_output
        )


if __name__ == '__main__':
    unittest.main()
