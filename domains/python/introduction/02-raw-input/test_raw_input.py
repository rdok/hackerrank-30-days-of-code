import unittest
import subprocess
from ddt import ddt, data

@ddt
class TestRawInput(unittest.TestCase):

    @data('How many chickens does it take to cross the road?\n', 'other-text\n')
    def test_prints_raw_input(self, value):

        expectedOuput =  value

        process = subprocess.Popen(["python", "raw_input.py"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)

        actualOuput = process.communicate(input=expectedOuput)[0]

        self.assertEquals(expectedOuput, actualOuput);

if __name__ == '__main__':
    unittest.main()
