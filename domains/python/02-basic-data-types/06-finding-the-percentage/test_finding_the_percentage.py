import os
import subprocess
import unittest


class TestFindingPercentage(unittest.TestCase):
    def setUp(self):
        script = os.path.dirname(
            os.path.realpath(__file__)) + "/finding_the_percentage.py"

        self.process = subprocess.Popen(
            ["python", script],
            stdout=subprocess.PIPE, stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )

    def tearDown(self):
        self.process = None

    def test_two_students(self):
        # Given you have a record of some students
        # And each recording the name, percent mark in maths, physics, and
        # chemistry. Mark number type: float
        # And the user enters the number of students
        # And followed by the names and marks of the students 
        # When you save these records to a dictionary 
        # And the user enters a student's name 
        actual_output = self.process.communicate(
            input='3\nKrishna 67 68 69\nArjun 70 98 63\nMalika 52 56 '
                  '60\nMalika\n '
        )[0]

        # Then I should see the average percent marks obtained by that student
        # correct to two decimal places.
        self.assertEquals('56.00\n', actual_output)


if __name__ == '__main__':
    unittest.main()
