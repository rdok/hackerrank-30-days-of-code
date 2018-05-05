import os
import subprocess
import unittest


class TestMutations(unittest.TestCase):
    def setUp(self):
        script = os.path.dirname(os.path.realpath(__file__)) + "/mutations.py"

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
            input='abracadabra\n5 k\n'
        )[0]

        self.assertEquals('abrackdabra\n', actual_output);


if __name__ == '__main__':
    unittest.main()
