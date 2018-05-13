from src.hackerrank.p02_basic_data_types.p06_finding_the_percentage import finding_the_percentage

from tests.test_case import TestCase


class TestFindingPercentage(TestCase):
    def setUp(self):
        self.script = finding_the_percentage.__file__

    def test_two_students(self):
        # Given you have a record of some students
        # And each recording the name, percent mark in maths, physics, and
        # chemistry. Mark number type: float
        # And the user enters the number of students
        # And followed by the names and marks of the students 
        # When you save these records to a dictionary 
        # And the user enters a student's name
        user_input = '3\nKrishna 67 68 69\nArjun 70 98 63\nMalika 52 56 60\nMalika\n '

        actual_output = self.execute(self.script, user_input)

        # Then I should see the average percent marks obtained by that student
        # correct to two decimal places.
        self.assertEquals('56.00\n', actual_output)
