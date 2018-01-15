import os
import subprocess
import unittest

from ddt import ddt, data


@ddt
class TestRawInput(unittest.TestCase):
    @data('How many chickens does it take to cross the road?\n', 'other-text\n')
    def test_prints_raw_input(self, value):
        expected_output = value
        dir_path = os.path.dirname(os.path.realpath(__file__))

        process = subprocess.Popen(
            ["python", dir_path + "/raw_input.py"],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )

        actual_output = process.communicate(input=expected_output)[0]

        self.assertEquals(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
