import subprocess
import unittest


class TestStringValidators(unittest.TestCase):
    def setUp(self):
        self.process = subprocess.Popen(
            ["python", "string_validators.py"],
            stdout=subprocess.PIPE, stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )

    def tearDown(self):
        self.process = None

    def test_default_case(self):
        actual_output = self.process.communicate(input='qA2\n')[0]
        self.assertEquals('True\nTrue\nTrue\nTrue\nTrue\n', actual_output)

    def test_only_alphabetical(self):
        actual_output = self.process.communicate(input='qA\n')[0]
        self.assertEquals('True\nTrue\nFalse\nTrue\nTrue\n', actual_output)

    def test_only_digit(self):
        actual_output = self.process.communicate(input='134\n')[0]
        self.assertEquals('True\nFalse\nTrue\nFalse\nFalse\n', actual_output)

    def test_only_lower(self):
        actual_output = self.process.communicate(input='lower\n')[0]
        self.assertEquals('True\nTrue\nFalse\nTrue\nFalse\n', actual_output)

    def test_only_upper(self):
        actual_output = self.process.communicate(input='UPPER\n')[0]
        self.assertEquals('True\nTrue\nFalse\nFalse\nTrue\n', actual_output)


if __name__ == '__main__':
    unittest.main()
