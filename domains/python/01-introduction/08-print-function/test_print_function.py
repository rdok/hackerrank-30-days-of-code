import subprocess
import unittest

from ddt import ddt


@ddt
class TestPrintFunction(unittest.TestCase):
    def test_is_evenly_dived(self):
        process = subprocess.Popen(["python", "print_function.py"],
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)

        actual_ouput = process.communicate(input='3')[0]

        self.assertEquals('123\n', actual_ouput)


if __name__ == '__main__':
    unittest.main()
