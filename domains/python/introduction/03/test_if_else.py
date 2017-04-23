import unittest
import subprocess
from ddt import ddt, data

@ddt
class TestIfElse(unittest.TestCase):

    @data('1', '3', '6', '20')
    def test_weird_numbers(self, rawInput):

        process = subprocess.Popen(["python", "if_else.py"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)

        actualOuput = process.communicate(input=rawInput)[0]

        self.assertEquals("Weird\n", actualOuput);

    @data('2', '4', '22', '100')
    def test_not_weird_numbers(self, rawInput):

        process = subprocess.Popen(["python", "if_else.py"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)

        actualOuput = process.communicate(input=rawInput)[0]

        self.assertEquals("Not Weird\n", actualOuput);

if __name__ == '__main__':
    unittest.main()
