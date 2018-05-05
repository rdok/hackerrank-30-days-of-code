import os
import subprocess
import unittest


class TestStringSplitAndJoin(unittest.TestCase):
    def setUp(self):
        script = os.path.dirname(os.path.realpath(__file__)) \
                 + "/string_split_and_join.py"

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
            input='this is a string\n'
        )[0]

        self.assertEquals('this-is-a-string\n', actual_output)


if __name__ == '__main__':
    unittest.main()
