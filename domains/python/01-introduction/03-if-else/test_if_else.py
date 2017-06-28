import subprocess
import unittest

from ddt import ddt, data


@ddt
class TestIfElse(unittest.TestCase):
    @data('1', '3', '6', '20')
    def test_weird_numbers(self, raw_input):
        process = subprocess.Popen(
            ["python", "if_else.py"],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )

        actual_output = process.communicate(input=raw_input)[0]

        self.assertEquals("Weird\n", actual_output)

    @data('2', '4', '22', '100')
    def test_normal_numbers(self, rawInput):
        process = subprocess.Popen(
            ["python", "if_else.py"],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )

        actual_output = process.communicate(input=rawInput)[0]

        self.assertEquals("Not Weird\n", actual_output)


if __name__ == '__main__':
    unittest.main()
