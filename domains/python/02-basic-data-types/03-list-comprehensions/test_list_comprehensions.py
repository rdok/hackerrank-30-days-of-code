import subprocess
import unittest


class TestTuples(unittest.TestCase):
    def setUp(self):
        self.process = subprocess.Popen(
            ["python", "list_comprehensions.py"],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )

    def tearDown(self):
        self.process = None

    def test_use_case(self):
        actual_output = self.process.communicate(input='1\n1\n1\n2\n')[0]
        self.assertEquals(
            '[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]\n',
            actual_output
        )

    def test_use_case_custom_1(self):
        actual_output = self.process.communicate(input='2\n3\n4\n5\n')[0]
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
            actual_output
        )


if __name__ == '__main__':
    unittest.main()
