from src.p02_basic_data_types.p05_nested_lists import nested_lists

from tests.test_case import TestCase


class TestFindSecondLowestGrade(TestCase):
    def setUp(self):
        self.script = nested_lists.__file__

    def test_two_students(self):
        # Given the name and grade of two students
        output = self.execute(self.script, '2\nHarry\n37.21\nBerry\n37.2')

        # Then I see the name of this student with the lowest grade
        self.assertEquals('Berry\n', output)

    def test_three_students(self):
        # Given the name and grade of three students
        user_input = '3\nHarry\n37.21\nBerry\n37.2\nTina\n37.5'
        actual = self.execute(self.script, user_input)

        # Then I see the name of the student with the second lowest grade
        self.assertEquals('Harry\n', actual)

    def test_three_students_sorted(self):
        user_input = '3\nHarrya\n37.21\nHarryb\n37.21\nBerry\n37.2\nTina\n37.5'
        actual = self.execute(self.script, user_input)
        self.assertEquals('Harrya\nHarryb\n', actual)

    def test_with_multiple_lowest_grade(self):
        # Given I have 4 students with two lowest grades
        user_input = '4\nHarryb\n37.21\nHarrya\n37.2\nBerry\n37.2\nTina\n37.5'
        actual = self.execute(self.script, user_input)
        # Then I see the name of the student with the second lowest grade
        self.assertEquals('Harryb\n', actual)

    def test_with_mutliple_second_lowest_grade(self):
        # Given I have 3 students with two second lowest grades
        user_input = '3\nTest1\n52\nTest2\n53\nTest3\n53'
        actual = self.execute(self.script, user_input)

        # Then I see the name of the student with the second lowest grade
        self.assertEquals('Test2\nTest3\n', actual)
