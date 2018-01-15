import os
import subprocess
import unittest


class TestFindAString(unittest.TestCase):
    def setUp(self):
        script = os.path.dirname(
            os.path.realpath(__file__)) + "/find_a_string.py"

        self.process = subprocess.Popen(
            ["python", script],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )

    def tearDown(self):
        self.process = None

    def test_default_case(self):
        actual_output = self.process.communicate(
            input='ABCDCDC\nCDC\n'
        )[0]

        self.assertEquals('2\n', actual_output)


if __name__ == '__main__':
    unittest.main()
