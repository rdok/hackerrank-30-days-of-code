import unittest
import subprocess

class TestFindSecondLargestNumber(unittest.TestCase):

    def setUp(self):
        self.process = subprocess.Popen(
            ["python", "find_second_largest_number.py"],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )

    def tearDown(self):
        self.process = None

    def test_use_case(self):
        actualOuput = self.process.communicate( input = '5\n2 3 6 6 5' )[0]
        self.assertEquals('5\n', actualOuput); 

    def test_use_case_1(self):
        actualOuput = self.process.communicate( input = '5\n2 3 6 -6 5' )[0]
        self.assertEquals('5\n', actualOuput); 

    def test_use_case_1(self):
        actualOuput = self.process.communicate( input = '5\n-2 -3 -6 -6 -5' )[0]
        self.assertEquals('-3\n', actualOuput); 

if __name__ == '__main__':
    unittest.main()
