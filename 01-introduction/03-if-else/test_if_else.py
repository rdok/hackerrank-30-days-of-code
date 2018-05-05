import os
import subprocess
import unittest

from ddt import ddt, data


@ddt
class TestIfElse(unittest.TestCase):
    @data('1', '3', '6', '20')
    def test_weird_numbers(self, weird_number):
        self.assertEquals("Weird\n", self.execute_script(weird_number))

    @data('2', '4', '22', '100')
    def test_normal_numbers(self, normal_number):
        self.assertEquals("Not Weird\n", self.execute_script(normal_number))

    @staticmethod
    def execute_script(argument):
        script = os.path.dirname(os.path.realpath(__file__)) + "/if_else.py"

        process = subprocess.Popen(
            ["python", script],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )

        return process.communicate(input=argument)[0]


if __name__ == '__main__':
    unittest.main()
