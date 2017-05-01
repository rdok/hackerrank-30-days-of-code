import unittest
import subprocess

class TestTuples(unittest.TestCase):

    def setUp(self):
        self.process = subprocess.Popen(
            ["python", "list_comprehensions.py"],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )

    def tearDown(self):
        self.process = None

    def test_use_case(self):
        actualOuput = self.process.communicate( input = '1\n1\n1\n2\n' )[0]
        self.assertEquals(
            '[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]',
            actualOuput
        ); 

if __name__ == '__main__':
    unittest.main()
