import unittest
import subprocess

class TestFindSecondLowestGrade(unittest.TestCase):

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
            input = '3\nHarry\n37.21\nBerry\n37.2\nTina\n37.5' )[0]

        # Then I see the name of the student with the second lowest grade
        self.assertEquals('Harry\n', actualOuput); 

    def test_three_students_sorted(self):
        actualOuput = self.process.communicate( 
            input = '3\nHarrya\n37.21\nHarryb\n37.21\nBerry\n37.2\nTina\n37.5' )[0]

        self.assertEquals('Harrya\nHarryb\n', actualOuput); 

    def test_with_multiple_lowest_grade(self):
        # Given I have 4 students with two lowest grades
        actualOuput = self.process.communicate( 
            input = '4\nHarryb\n37.21\nHarrya\n37.2\nBerry\n37.2\nTina\n37.5' )[0]

        # Then I see the name of the student with the second lowest grade
        self.assertEquals('Harryb\n', actualOuput); 

    def test_with_mutliple_second_lowest_grade(self):
        # Given I have 3 students with two second lowest grades
        actualOuput = self.process.communicate( 
            input = '3\nTest1\n52\nTest2\n53\nTest3\n53' )[0]

        # Then I see the name of the student with the second lowest grade
        self.assertEquals('Test2\nTest3\n', actualOuput); 


if __name__ == '__main__':
    unittest.main()
