import subprocess
import unittest


class TestStringMethods(unittest.TestCase):
    def test_see_expected_string(self):
        process = subprocess.Popen(
            ["python", "hello.py"], stdout=subprocess.PIPE
        )

        actual_output = process.communicate()[0]

        self.assertEqual('Hello, World!\n', actual_output)


if __name__ == '__main__':
    unittest.main()
