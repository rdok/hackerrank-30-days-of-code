from src.codeacademy.learn_python.p01_python_syntax import p10_two_types_of_division
from tests.test_case import TestCase


class TwoTypesOfDivisionTest(TestCase):
    def setUp(self):
        self.script = p10_two_types_of_division
        self.cucumbers = 100
        self.num_people = 6
        self.whole_cucumbers_per_person = self.cucumbers / self.num_people

    def test_it_holds_cucumbers_and_number_of_people(self):
        self.assertIsInstance(self.script.cucumbers, int)
        self.assertEqual(self.cucumbers, self.script.cucumbers)
        self.assertIsInstance(self.script.num_people, int)
        self.assertEqual(self.num_people, self.script.num_people)

    def test_it_holds_whole_cucumbers_per_person(self):
        self.assertIsInstance(self.script.whole_cucumbers_per_person, int)
        self.assertEqual(
            self.whole_cucumbers_per_person,
            self.script.whole_cucumbers_per_person
        )

    def test_it_prints_whole_cucumbers_per_person(self):
        printed_response = self.execute(self.script.__file__)
        expected_response = str(self.whole_cucumbers_per_person) + "\n"
        self.assertEqual(expected_response, printed_response)
