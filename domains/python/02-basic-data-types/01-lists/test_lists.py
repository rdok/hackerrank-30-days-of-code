import subprocess
import unittest

from ddt import ddt


@ddt
class TestLists(unittest.TestCase):
    def setUp(self):
        self.process = subprocess.Popen(
            ["python", "lists.py"],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )

    def tearDown(self):
        self.process = None

    def test_zero_commands(self):
        actual_output = self.process.communicate(input='0\n')[0]
        self.assertEquals('', actual_output)

    def test_two_commands(self):
        actual_output = self.process.communicate(
            input='2\ninsert 0 5\nprint\n'
        )[0]

        self.assertEquals('[5]\n', actual_output)

    def test_print(self):
        actual_output = self.process.communicate(
            input='2\ninsert 0 5\nprint\n'
        )[0]

        self.assertEquals('[5]\n', actual_output)

    def test_insert(self):
        actual_output = self.process.communicate(
            input='2\ninsert 0 5\nprint\n'
        )[0]

        self.assertEquals('[5]\n', actual_output)

    def test_remove(self):
        actual_output = self.process.communicate(
            input='4\ninsert 0 5\ninsert 1 10\nremove 5\nprint\n'
        )[0]

        self.assertEquals('[10]\n', actual_output
                          )

    def test_append(self):
        actualOuput = self.process.communicate(input='2\nappend 10\nprint\n')[0]
        self.assertEquals('[10]\n', actualOuput)

    def test_sort(self):
        actual_output = self.process.communicate(
            input='3\nappend 10\nappend 5\nprint\n'
        )[0]

        self.assertEquals('[10, 5]\n', actual_output)

        process = subprocess.Popen(
            ["python", "lists.py"],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )

        actual_output = process.communicate(
            input='4\nappend 10\nappend 5\nsort\nprint\n'
        )[0]

        self.assertEquals('[5, 10]\n', actual_output)

    def test_pop(self):
        actual_output = self.process.communicate(
            input='3\nappend 10\npop\nprint\n'
        )[0]

        self.assertEquals('[]\n', actual_output)

    def test_reverse(self):
        actual_output = self.process.communicate(
            input='4\nappend 10\nappend 5\nreverse\nprint\n'
        )[0]

        self.assertEquals('[5, 10]\n', actual_output)

    def test_case_1(self):
        actual_output = self.process.communicate(
            input='12\ninsert 0 5\ninsert 1 10\ninsert 0 6\nprint\nremove '
                  '6\nappend 9\nappend 1\nsort\nprint\npop\nreverse\nprint\n'
        )[0]

        self.assertEquals(
            '[6, 5, 10]\n[1, 5, 9, 10]\n[9, 5, 1]\n',
            actual_output
        )


if __name__ == '__main__':
    unittest.main()
