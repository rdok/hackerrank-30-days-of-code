import os
import subprocess
import unittest


class TestStringMethods(unittest.TestCase):
    def test_see_expected_string(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        process = subprocess.Popen(
            ["python", dir_path + "/hello.py"],
            stdout=subprocess.PIPE
        )

        actual_output = process.communicate()[0].rstrip()

        self.assertEqual('Hello, World!', actual_output)


if __name__ == '__main__':
    unittest.main()
