import os
import subprocess
import unittest


class TestTextWrap(unittest.TestCase):
    def setUp(self):
        script = os.path.dirname(os.path.realpath(__file__)) + "/text_wrap.py"

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
            input='ABCDEFGHIJKLIMNOQRSTUVWXYZ\n4\n'
        )[0]

        self.assertEquals(
            "ABCD\nEFGH\nIJKL\nIMNO\nQRST\nUVWX\nYZ\n",
            actual_output
        )


if __name__ == '__main__':
    unittest.main()
