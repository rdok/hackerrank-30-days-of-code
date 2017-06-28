import subprocess
import unittest


class TestFindAString(unittest.TestCase):
    def setUp(self):
        self.process = subprocess.Popen(
            ["python", "find_a_string.py"],
            stdout=subprocess.PIPE, stdin=subprocess.PIPE,
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
