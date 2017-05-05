import unittest
import subprocess

class TestFindSecondLargestNumber(unittest.TestCase):

    def setUp(self):
        self.process = subprocess.Popen( ["python", "nested_lists.py"],
            stdout=subprocess.PIPE, stdin=subprocess.PIPE, 
            stderr=subprocess.STDOUT 
        )

    def tearDown(self):
        self.process = None

    def test_two_students(self):
        # Given the name and grade of two students
        actualOuput = self.process.communicate( 
            input = '2\nHarry\n37.21\nBerry\n37.2' )[0]

        # Then I see the name of this student with the lowest grade
        self.assertEquals('Berry\n', actualOuput); 

    def test_three_students(self):
        # Given the name and grade of three students
        actualOuput = self.process.communicate( 
            input = '2\nHarry\n37.21\nBerry\n37.2\nTina\n37.5' )[0]

        # Then I see the name of this student with the lowest grade
        self.assertEquals('Harry\n', actualOuput); 

if __name__ == '__main__':
    unittest.main()
