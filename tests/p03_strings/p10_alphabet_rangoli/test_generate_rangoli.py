import os

from src.p03_strings.p10_alphabet_rangoli.generate_rangoli import GenerateRangoli
from tests import test_case


class TestGenerateRangoli(test_case.TestCase):

    def setUp(self):
        self.generateRangoli = GenerateRangoli()

    def test_rangoli_of_size_zero(self):
        self.assertEquals('', self.generateActualOutput(0))

    def test_rangoli_of_size_one(self):
        actual = self.generateActualOutput(1)
        expected = self.generateExpectedOutput("case_01.txt")

        self.assertEquals(expected, actual)

    def test_rangoli_of_size_two(self):
        actual = self.generateActualOutput(2)
        expected = self.generateExpectedOutput("case_02.txt")

        self.assertEquals(expected, actual)

    def test_rangoli_of_size_three(self):
        actual = self.generateActualOutput(3)
        expected = self.generateExpectedOutput("case_03.txt")

        self.assertEquals(expected, actual)

    def test_rangoli_of_size_five(self):
        actual = self.generateActualOutput(5)
        expected = self.generateExpectedOutput("case_05.txt")

        self.assertEquals(expected, actual)

    def test_it_stiches_a_rangoli_layer_of_index_0(self):
        structure = [['-' for x in range(5)] for x in range(3)]
        actual = self.generateRangoli.stitch_rangoli_line(0, 1, 2, structure)
        structure[1][3] = 'a'
        expected = structure

        self.assertEquals(expected, actual)

    def test_it_stiches_a_rangoli_layer_of_index_1(self):
        structure = [['-' for x in range(5)] for x in range(3)]
        actual = self.generateRangoli.stitch_rangoli_line(1, 1, 2, structure)
        expected = [
            ['-', '-', 'b', '-', '-'],
            ['b', '-', '-', '-', 'b'],
            ['-', '-', 'b', '-', '-'],
        ]

        self.assertEquals(expected, actual)

    def test_it_stiches_a_rangoli_layer_of_index_2(self):
        structure = [['-' for x in range(9)] for x in range(5)]
        expected = [
            ['-', '-', '-', '-', 'c', '-', '-', '-', '-'],
            ['-', '-', 'c', '-', '-', '-', 'c', '-', '-'],
            ['c', '-', '-', '-', '-', '-', '-', '-', 'c'],
            ['-', '-', 'c', '-', '-', '-', 'c', '-', '-'],
            ['-', '-', '-', '-', 'c', '-', '-', '-', '-'],
        ]
        actual = self.generateRangoli.stitch_rangoli_line(2, 2, 4, structure)

        self.assertEquals(expected, actual)

    def test_it_finalizes_a_rangolie(self):
        expected = '--\n--\n--'
        actual = self.generateRangoli.finalize_rangoli([['-'] * 2] * 3)

        self.assertEquals(expected, actual)

    def test_it_creates_a_rangoli_structure(self):
        expected = [['-' for x in range(3)] for x in range(2)]
        actual = self.generateRangoli.create_structure(2, 3)

        self.assertEquals(expected, actual)

    def generateActualOutput(self, size):
        return self.generateRangoli.handle(size)

    def generateExpectedOutput(self, file_name):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        case_path = os.path.join(current_directory, file_name)
        return self.file_contents(case_path)
