import unittest
import subprocess
from ddt import ddt, data, unpack

@ddt
class TestArithmetciOperators(unittest.TestCase):

    @unpack
    @data({ 'firstInput': '1', 'secondInput': '3', 'total': '4', 'difference': '-2', 'product': '3' },
          { 'firstInput': '3', 'secondInput': '2', 'total': '5', 'difference': '1', 'product': '6' })
    def test_sum_of_numbers(self, firstInput, secondInput, total, difference, product):

        process = subprocess.Popen(["python", "arithmetic_operators.py"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)

        actualOuput = process.communicate( input = firstInput + '\n' + secondInput + '\n')[0]

        self.assertEquals(total + '\n' + difference + '\n' + product + '\n', actualOuput);

if __name__ == '__main__':

    unittest.main()
