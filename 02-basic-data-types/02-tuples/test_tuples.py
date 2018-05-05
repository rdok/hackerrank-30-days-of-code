import os
import subprocess
import unittest


class TestTuples(unittest.TestCase):
    def setUp(self):
        script = os.path.dirname(os.path.realpath(__file__)) + "/tuples.py"

        self.process = subprocess.Popen(
            ["python", script],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )

    def tearDown(self):
        self.process = None

    def test_use_case(self):
        actual_output = self.process.communicate('2\n1 2\n')[0]

        self.assertEquals('3713081631934410656\n', actual_output)


if __name__ == '__main__':
    unittest.main()
