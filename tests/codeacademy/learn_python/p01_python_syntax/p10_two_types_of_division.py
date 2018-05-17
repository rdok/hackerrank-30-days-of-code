from src.codeacademy.learn_python.p01_python_syntax import p10_two_types_of_division
from tests.test_case import TestCase


class TwoTypesOfDivisionTest(TestCase):
    def setUp(self):
        self.script = p10_two_types_of_division
        self.cucumbers = 100
        self.num_people = 6

    def test_it_holds_cucumbers_and_number_of_people(self):
        self.assertIsInstance(self.script.cucumbers, int)
        self.assertEqual(self.cucumbers, self.script.cucumbers)
        self.assertIsInstance(self.script.num_people, int)
        self.assertEqual(self.num_people, self.script.num_people)
