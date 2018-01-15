import os
import subprocess
import unittest


class TestSwapCase(unittest.TestCase):
    def setUp(self):
        script = os.path.dirname(os.path.realpath(__file__)) + "/swap_case.py"

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
            input='HackerRank.com presents "Pythonist 2".\n'
        )[0]

        self.assertEquals(
            'hACKERrANK.COM PRESENTS "pYTHONIST 2".\n',
            actual_output
        )


if __name__ == '__main__':
    unittest.main()
