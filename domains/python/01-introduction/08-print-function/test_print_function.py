import os
import subprocess
import unittest

from ddt import ddt


@ddt
class TestPrintFunction(unittest.TestCase):
    def test_is_evenly_dived(self):
        script = os.path.dirname(os.path.realpath(__file__)) \
                 + "/print_function.py"

        process = subprocess.Popen(["python", script],
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)

        actual_output = process.communicate(input='3')[0]

        self.assertEquals('123\n', actual_output)


if __name__ == '__main__':
    unittest.main()
