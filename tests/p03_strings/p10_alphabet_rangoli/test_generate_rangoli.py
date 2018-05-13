from unittest_data_provider import data_provider

from src.p03_strings.p10_alphabet_rangoli.generate_rangoli import GenerateRangoli
from tests.test_case import TestCase


# See https://www.hackerrank.com/challenges/alphabet-rangoli/problem
class TestGenerateRangoli(TestCase):
    frame_data_provider = lambda: (
        # (size, expected)
        (0, {"width": 0, "height": 0, "x_center": 0, "y_center": 0}),
        (1, {"width": 1, "height": 1, "x_center": 0, "y_center": 0}),
        (2, {"width": 5, "height": 3, "x_center": 2, "y_center": 1}),
        (3, {"width": 9, "height": 5, "x_center": 4, "y_center": 2}),
    )

    canvas_data_provider = lambda: (
        # (expected, rows, columns)
        ([], 0, 0),
        ([['-']], 1, 1),
        ([['-', '-', '-', '-', '-'],
          ['-', '-', '-', '-', '-'],
          ['-', '-', '-', '-', '-'], ], 3, 5),
    )

    def setUp(self):
        self.generateRangoli = GenerateRangoli()

    @data_provider(frame_data_provider)
    def test_it_generates_rangoli_frame(self, size, expected):
        actual = self.generateRangoli.create_frame(size)
        self.assertEquals(expected, actual)

    @data_provider(canvas_data_provider)
    def test_it_generates_rangoli_canvas(self, expected, width, height):
        actual = self.generateRangoli.create_canvas(width, height)
        self.assertEquals(expected, actual)

    def test_rangoli_of_size_zero(self):
        self.assertEquals('', self.generateActualOutput(0))

    def test_rangoli_of_size_one(self):
        actual = self.generateActualOutput(1)
        expected = self.generateExpectedOutput(__file__, "case_01.txt")

        self.assertEquals(expected, actual)

    def test_rangoli_of_size_two(self):
        actual = self.generateActualOutput(2)
        expected = self.generateExpectedOutput(__file__, "case_02.txt")

        self.assertEquals(expected, actual)

    def test_rangoli_of_size_three(self):
        actual = self.generateActualOutput(3)
        expected = self.generateExpectedOutput(__file__, "case_03.txt")

        self.assertEquals(expected, actual)

    def test_rangoli_of_size_five(self):
        actual = self.generateActualOutput(5)
        expected = self.generateExpectedOutput(__file__, "case_05.txt")

        self.assertEquals(expected, actual)

    def test_it_stiches_a_rangoli_layer_of_index_0(self):
        structure = [['-' for x in range(5)] for x in range(3)]
        actual = self.generateRangoli.stitch_rangoli_line('a', 0, 1, 2, structure)
        structure[0][0] = 'a'
        expected = structure

        self.assertEquals(expected, actual)

    def test_it_stiches_a_rangoli_layer_of_index_1(self):
        structure = [['-' for x in range(5)] for x in range(3)]
        actual = self.generateRangoli.stitch_rangoli_line('b', 1, 1, 2, structure)
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
        actual = self.generateRangoli.stitch_rangoli_line('c', 2, 2, 4, structure)

        self.assertEquals(expected, actual)

    def test_it_finalizes_a_rangolie(self):
        expected = '--\n--\n--'
        actual = self.generateRangoli.convert_to_text([['-'] * 2] * 3)

        self.assertEquals(expected, actual)

    def test_it_creates_a_rangoli_structure(self):
        expected = [['-' for x in range(3)] for x in range(2)]
        actual = self.generateRangoli.create_canvas(2, 3)

        self.assertEquals(expected, actual)

    def generateActualOutput(self, size):
        return self.generateRangoli.handle(size)
