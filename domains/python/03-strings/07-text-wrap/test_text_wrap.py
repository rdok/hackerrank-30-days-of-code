import subprocess
import unittest


class TestTextWrap(unittest.TestCase):
    def setUp(self):
        self.process = subprocess.Popen(
            ["python", "text_wrap.py"],
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
