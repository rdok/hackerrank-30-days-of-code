from src.p02_basic_data_types.p03_list_comprehensions import list_comprehensions

from tests.test_case import TestCase


class TestTuples(TestCase):
    def setUp(self):
        self.script = list_comprehensions.__file__

    def test_use_case(self):
        expected = '[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]\n'
        actual = self.execute(self.script, '1\n1\n1\n2\n')
        self.assertEquals(expected, actual)

    def test_use_case_custom_1(self):
        actual = self.execute(self.script, '2\n3\n4\n5\n')

        self.assertEquals(
            '[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 0, 3], [0, 0, 4], [0, 1, '
            '0], [0, 1, 1], [0, 1, 2], [0, 1, 3], [0, 2, 0], [0, 2, 1], [0, '
            '2, 2], [0, 2, 4], [0, 3, 0], [0, 3, 1], [0, 3, 3], [0, 3, 4], '
            '[1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 0, 3], [1, 1, 0], [1, 1, '
            '1], [1, 1, 2], [1, 1, 4], [1, 2, 0], [1, 2, 1], [1, 2, 3], [1, '
            '2, 4], [1, 3, 0], [1, 3, 2], [1, 3, 3], [1, 3, 4], [2, 0, 0], '
            '[2, 0, 1], [2, 0, 2], [2, 0, 4], [2, 1, 0], [2, 1, 1], [2, 1, '
            '3], [2, 1, 4], [2, 2, 0], [2, 2, 2], [2, 2, 3], [2, 2, 4], [2, '
            '3, 1], [2, 3, 2], [2, 3, 3], [2, 3, 4]]\n',
            actual
        )
