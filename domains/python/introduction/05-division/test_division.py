import unittest
import subprocess
from ddt import ddt, data, unpack

@ddt
class TestDivision(unittest.TestCase):

    @unpack
    @data( [ '4', '3', '1\n1.33333333333\n' ] )
    def test_division_types(self, firstInput, secondInput, expectedOutput):

        process = subprocess.Popen(["python", "division.py"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)

        actualOuput = process.communicate( input = firstInput + '\n' + secondInput + '\n')[0]

        self.assertEquals(expectedOutput, actualOuput);

if __name__ == '__main__':

    unittest.main()
