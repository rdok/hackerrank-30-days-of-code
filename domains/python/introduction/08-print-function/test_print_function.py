import unittest
from ddt import ddt, data, unpack
import subprocess

@ddt
class TestPrintFunction(unittest.TestCase):

    def test_is_evenly_dived(self):
        process = subprocess.Popen(["python", "print_function.py"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
        actualOuput = process.communicate( input = '3' )[0]
        self.assertEquals('123\n', actualOuput); 

if __name__ == '__main__':
    unittest.main()
