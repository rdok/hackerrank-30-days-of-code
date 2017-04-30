import unittest
import subprocess

class TestTuples(unittest.TestCase):

    def setUp(self):
        self.process = subprocess.Popen(
            ["python", "tuples.py"],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )

    def tearDown(self):
        self.process = None

    def test_use_case(self):
        actualOuput = self.process.communicate( input = '2\n1 2\n' )[0]
        self.assertEquals('3713081631934410656\n', actualOuput); 

if __name__ == '__main__':
    unittest.main()
